# Crear un Flujo de Carga

En el rol de desarrollador senior en CXC, la creación de flujos de carga de datos (ETL) es una tarea fundamental. Estos flujos automatizados desempeñan un papel crucial en la integración de datos, extrayéndolos de diversas fuentes, transformándolos según las necesidades del análisis y cargándolos en un destino final, generalmente una base de datos. Un ETL se compone de tres etapas esenciales: extracción, transformación y carga.
**Tu objetivo principal será desarrollar un ETL básico que implemente el siguiente flujo:**

1.  **Leer un archivo con extensión (.csv, .xlsx, etc.):** El primer paso consiste en extraer los datos de un archivo en formato CSV, Excel u otro formato compatible.
    
2.  **Aplicar reglas de negocio sobre cada una de las filas:** A continuación, se aplicarán las reglas de negocio definidas para cada fila del archivo, asegurando la integridad y consistencia de los datos.
    
3.  **Transformar la fila en un objeto de negocio:** Cada fila del archivo será transformada en un objeto de negocio, representando una entidad específica dentro del sistema.
    
4.  **Descartar los objetos duplicados:** Se identificarán y eliminarán los objetos duplicados, garantizando que solo se almacenen registros únicos en el sistema.
    
5.  **Persistir los objetos de negocio válidos en una fuente de datos:** Finalmente, los objetos de negocio válidos se almacenarán de forma permanente en una fuente de datos, como una base de datos relacional.

## Casos de Uso

### 1. Generar el esquema de base de datos a partir del archivo: `ejercicio_ddl.txt` (contenido en .zip para la prueba)

### 2. Carga de Catálogos para Validación de Información

**Contexto:**

Los catálogos son conjuntos de datos estructurados que sirven como diccionarios de referencia para la validación y enriquecimiento de información. En este caso, se utilizan catálogos para garantizar la precisión de los datos de empleados.

**Estructura del Catálogo:**

Cada catálogo se almacena en una tabla SQL separada, siguiendo un esquema común:

-   La columna `id` representa la clave única de cada elemento del catálogo.
    
-   La columna `name` almacena el nombre descriptivo del elemento del catálogo.
    

**Catálogos a Cargar:**

-   `test.agency`: Almacena nombres de agencias.
    
-   `test.profession`: Almacena títulos profesionales.
    
-   `test.ethnicity`: Almacena etnias.
    
-   `test.gender`: Almacena géneros.
    

**Archivo de Entrada:**

Los datos de los catálogos se encuentran en un archivo CSV denominado `catalogos.csv`. (contenido en .zip para la prueba).

**Correspondencia entre Columnas:**

-   La columna `agency_name` del archivo CSV se corresponde con la columna `name` de la tabla `test.agency`.
    
-   La columna `class_title` del archivo CSV se corresponde con la columna `name` de la tabla `test.profession`.
    
-   La columna `ethnicity` del archivo CSV se corresponde con la columna `name` de la tabla `test.ethnicity`.
    
-   La columna `gender` del archivo CSV se corresponde con la columna `name` de la tabla `test.gender`.
    

**Objetivo:**

El objetivo de este paso es cargar los datos de los catálogos desde el archivo CSV `catalogos.csv` a las respectivas tablas SQL (`test.agency`,  `test.profession`,  `test.ethnicity`,  `test.gender`). Esto permitirá validar y enriquecer los datos de empleados en pasos posteriores.

### 3. Carga de Empleados Válidos

**Contexto:**

En este paso, se cargará una lista de empleados válidos desde un archivo CSV a la base de datos. Los datos de los empleados se validarán y enriquecerán utilizando los catálogos cargados previamente.

**Proceso de Carga:**

1.  **Lectura del Archivo CSV:** Se leerá el archivo `employees.csv`. (contenido en .zip para la prueba).
    
2.  **Transformación de Valores:** Para cada fila del archivo CSV, se transformarán los valores de las columnas `agency_name`,  `class_title` (profesión),  `ethnicity` y `gender` en claves de los catálogos correspondientes. Esto asegura la integridad y consistencia de los datos.

| Columna CSV               | Catálogo          | Valor Transformado                                           |
|---------------------------|-------------------|--------------------------------------------------------------|
| agency_name               | test.agency       | ID de la agencia correspondiente al nombre leído             |
| class_title (profesión)   | test.profession   | ID de la profesión correspondiente al título leído           |
| ethnicity                 | test.ethnicity    | ID de la etnia correspondiente al valor leído                |
| gender                    | test.gender       | ID del género correspondiente al valor leído                 |

    
3.  **Generación de Hash MD5:** Para cada objeto de empleado, se generará un hash MD5 utilizando los atributos `name`,  `last_name`,  `profession_id`,  `ethnicity_id` y `gender_id`. Este hash único servirá para identificar registros duplicados y evitar su carga en la base de datos.
    
4.  **Almacenamiento en la Base de Datos:** Los empleados válidos, junto con sus identificadores de catálogo y hash MD5, se almacenarán en la tabla `test.employee` de la base de datos.

**Prevención de Duplicados:**

El hash MD5 generado para cada empleado se utiliza para identificar registros duplicados. Si dos filas del archivo CSV generan el mismo hash MD5, se considera que son duplicados y solo se almacenará un registro en la base de datos.

**Objetivo:**

El objetivo de este paso es cargar una lista de empleados válidos y consistentes en la base de datos, asegurando la integridad de los datos y evitando registros duplicados.

### 4. Persistencia de Datos en Bloques de 10,000 Registros

**Explicación:**

En este paso, la información procesada se almacenará permanentemente en la base de datos. Para optimizar el rendimiento y la eficiencia del proceso de almacenamiento, se utilizarán bloques de 10,000 registros.

### 5. Entrega de la Solución del Ejercicio

Para completar este ejercicio, siga los siguientes pasos:

-   **Selección del Lenguaje de Programación:** Elija entre `Java` o `Python` como lenguaje de programación para implementar su solución. Puede utilizar cualquier framework o librería de su preferencia.
    
-   **Implementación de la Lógica:** Implemente la lógica necesaria para resolver el ejercicio de manera completa y correcta. Asegúrese de que su código esté bien estructurado y probado.
    
2.  **Subida a Repositorio Público:** Suba su solución completa a un repositorio público accesible, como GitHub o GitLab. Asegúrese de que el repositorio sea público y que el código esté correctamente versionado.
    
3.  **Envío del Enlace:** Envíe el enlace a su repositorio público al correo electrónico pepebbotella@gmail.com. El correo electrónico debe incluir su nombre completo, número de identificación (si corresponde) y una breve descripción de su solución