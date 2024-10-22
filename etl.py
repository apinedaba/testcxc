
import pandas as pd
from models import db, Agency, Profession, Ethnicity, Gender, Employee
import hashlib
from sqlalchemy.dialects.postgresql import insert


def cargar_catalogos(archivo_catalogos):
    data = pd.read_csv(archivo_catalogos)
    data = data.fillna('')
    for _, row in data.iterrows():
        if row['agency_name'] is not "":
            agency = insert(Agency).values({"name":row['agency_name']}).on_conflict_do_nothing(index_elements=['name'])
            db.session.execute(agency)            
        if row['class_title'] is not "":
            profession = insert(Profession).values({"name":row['class_title']}).on_conflict_do_nothing(index_elements=['name'])
            db.session.execute(profession)
        if  row['ethnicity'] is not "":              
            ethnicity = insert(Ethnicity).values({"name":row['ethnicity']}).on_conflict_do_nothing(index_elements=['name'])
            db.session.execute(ethnicity)
        if row['gender'] is not "":
            gender = insert(Gender).values({"name":row['gender']}).on_conflict_do_nothing(index_elements=['name'])
            db.session.execute(gender)                
    db.session.commit()
    return "Cargado"

def generate_hash_md5(employee):
    hash_str = f"{employee['name']}{employee['last_name']}{employee['profession_id']}{employee['ethnicity_id']}{employee['gender_id']}"
    return hashlib.md5(hash_str.encode()).hexdigest()

def cargar_empleados(filename):
    session = db.session
    data = pd.read_csv(filename)    
    agency_dict = {agency.name: agency.id for agency in session.query(Agency).all()}
    profession_dict = {profession.name: profession.id for profession in session.query(Profession).all()}
    ethnicity_dict = {ethnicity.name: ethnicity.id for ethnicity in session.query(Ethnicity).all()}
    gender_dict = {gender.name: gender.id for gender in session.query(Gender).all()}
    employees = []
    for _, row in data.iterrows():        
        profession_id = profession_dict.get(row['class_title'])
        agency_id = agency_dict.get(row['agency_name'])
        ethnicity_id = ethnicity_dict.get(row['ethnicity'])
        gender_id = gender_dict.get(row['gender'])        
        if not profession_id or not agency_id or not ethnicity_id or not gender_id:            
            continue        
        employee_data = {
            'name': row['name'],
            'last_name': row['last_name'],
            'agency_id': agency_id,
            'profession_id': profession_id,
            'ethnicity_id': ethnicity_id,
            'gender_id': gender_id
        }        
        employee_data['md5_hash'] = generate_hash_md5(employee_data)        
        employees.append(employee_data)   
    block_size = 10000
    response = []
    for i in range(0, len(employees), block_size):
        block = employees[i:i + block_size]        
        existing_hashes = session.query(Employee.md5_hash).filter(
            Employee.md5_hash.in_([emp['md5_hash'] for emp in block])
        ).all()
        existing_hashes = set(hash[0] for hash in existing_hashes)  

        
        block_to_insert = [emp for emp in block if emp['md5_hash'] not in existing_hashes]

        if block_to_insert:
            
            insert_stmt = insert(Employee).values(block_to_insert)
            insert_stmt = insert_stmt.on_conflict_do_nothing(index_elements=['md5_hash'])
            session.execute(insert_stmt)
            session.commit()

        response.append((f"Bloque {i // block_size + 1}: Insertados {len(block_to_insert)} empleados."))
    return response