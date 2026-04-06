# CONCEPTOS QUE CUESTAN

## Diferencia entre `WHERE`y `HAVING`
- `WHERE` filtra filas individuales antes de que se agrupen.

- `HAVING` filtra grupos después de que se hayan agrupado.

| Característica | WHERE | HAVING |
|:--- | :---: | ---: |
|¿Cuándo actúa?|Antes de agrupar.|Después de agrupar.|
|¿Sobre qué actúa?|Sobre filas individuales.|Sobre grupos o totales.|
|¿Puede usar agregados?|NO (No puedes hacer WHERE COUNT(*) > 5).|SÍ (Aquí es donde usas COUNT, SUM, AVG).|

<br>
El orden es:

1. SELECT
2. FROM
3. WHERE (Limpia los datos crudos)
4. GROUP BY (Agrupa)
5. HAVING (Limpia los resultados agrupados)
6. ORDER BY

## Cuándo aplicar los diferentes `JOIN`(`INNER JOIN`, `LEFT JOIN`, `JOIN ON`)

### *1. INNER JOIN (El filtro estricto)*
El INNER JOIN es el estándar. Solo devuelve registros cuando hay una coincidencia exacta en ambas tablas.

¿Cuándo usarlo? Cuando necesito la información de ambas partes obligatoriamente.

Ejemplo: Si quiero listar "Préstamos con el Nombre del Usuario", no sirve de nada un préstamo que no tenga un usuario asignado (eso sería un error de datos).

<ins>La Regla: "Si no hay pareja en ambos lados, descártalo."</ins>

### *2. LEFT JOIN (El conservador)*
El LEFT JOIN dice: "Muéstrame todo lo que hay en la tabla de la izquierda (la primera que menciono), y si encuentras algo relacionado en la derecha, ponlo. Si no, pon NULL".

¿Cuándo usarlo? Cuando la tabla de la derecha es opcional.

Ejemplo: Queremos listar todos los usuarios y ver si tienen multas. Si hago un INNER JOIN con multas, solo veré a los morosos (porque los usuarios sin multas no tienen pareja en la tabla multas). Con el LEFT JOIN, veré a todos los usuarios: los morosos con su multa, y los cumplidores con un NULL en el campo multa.

<ins>La Regla: "No pierdas a nadie de la tabla principal, aunque no tengan pareja."</ins>

### *3. El JOIN ON (La condición)*
JOIN ON no es un tipo distinto, es la sintaxis que usamos para unir tablas. Siempre debe ir acompañado de INNER o LEFT.

¿Qué hace el ON? Es el pegamento. Le dice a SQL: "Une estas dos tablas usando esta columna específica".

Ejemplo: ON usuarios.id = prestamos.usuario_id.

<ins>El truco: Es donde ocurre la "magia" de las llaves foráneas (FOREIGN KEY).</ins>
<br> <br>
|Situación|¿Qué JOIN elijo?|
| :--- | :--- |
|Necesito datos obligatorios de ambas tablas.|INNER JOIN|
|Quiero ver una lista completa (ej: todos los libros) y ver datos extras si existen.|LEFT JOIN|
|¿Qué columna uso para unir?|ON|


<br><br><br>
# Mi caja de herramientas
## 1. El esqueleto: Diseño y DDL
**Diseño** (Entidades/Relaciones/Normalización): Es la arquitectura. Si una tabla está bien diseñada, las consultas son mucho más fáciles.

**DDL** (CREATE TABLE, Constraints): Es la construcción. El PRIMARY KEY y FOREIGN KEY son los que permiten que los JOINs funcionen después.

## 2. El motor: DML y Transacciones
**DML** (INSERT INTO/UPDATE): Es el movimiento de datos. Aprendimos que siempre deben ir dentro de Transacciones (`BEGIN TRANSACTION;`/ `COMMIT;`) para asegurar que no queden datos a medias (como cuando ajusté la tabla de préstamos).

## 3. El análisis: Consultas, Agregaciones y Joins
SELECT, WHERE, ORDER BY, LIMIT: Los cimientos. El filtrado (WHERE) y el ordenado son la base de todo.

Agregaciones (COUNT, SUM, GROUP BY, HAVING): Es la inteligencia estadística. Nos permitió sacar el total de días o el número de multas.

JOINs (INNER, LEFT): Es la capacidad de conectar "islas" de datos. El LEFT JOIN fue clave para que los usuarios "buenos" no desaparecieran de los informes.

## 4. La potencia técnica: Funciones, Subconsultas y Vistas
### Funciones (DATE, JULIANDAY, CASE, CAST):

DATE/JULIANDAY: Para manejar el tiempo (indispensable para multas y préstamos).

CASE: Para crear lógica condicional (ej. marcar "A tiempo" vs "Retraso").

CAST: (Mi descubrimiento) Para transformar tipos de datos cuando el sistema necesita ayuda para calcular.

Subconsultas: Es el nivel avanzado. Nos permitieron filtrar libros usando la lógica de los autores, que es el inicio de los sistemas de recomendación.

Vistas (CREATE VIEW): (Lo mencionamos) Es la forma de guardar una consulta compleja como si fuera una tabla virtual, para no tener que escribir el código siempre.

# Funciones descubiertas y redescubiertas
### COALESCE(m.importe, 0)
 Esta función dice: "Si el importe es NULL (porque no hay multa), pon un 0". Así las sumas no fallan.

 ### CAST(... AS INTEGER)
 Con ella limpio los decimales de los días para que el informe se vea limpio.
 Con esta herramienta "obligoamos" a SQL a cambiar la forma de interpretar un dato antes de hacer una operación matemática o reporte.
 El comando CAST en SQL es básicamente un "traductor de tipos de datos".

Imagina que tienes un número que para SQL es un "texto" o un número con decimales que quieres tratar como "entero" (sin decimales). CAST le dice a la base de datos: "Toma este valor y conviértelo a este otro formato".

**La sintaxis** es muy sencilla:   
CAST(valor AS tipo_de_dato)

**Ejemplos prácticos:**
- Convertir un número a texto (para concatenar)
- Forzar números enteros:


**¿Cuándo es obligatorio usarlo?**   
Es obligatorio cuando el motor de base de datos es estricto y no sabe cómo sumar o comparar dos cosas de naturaleza distinta. Por ejemplo, en algunos sistemas, no puedes sumar un número y un texto directamente; primero tienes que usar CAST para que ambos sean números.

### julianday()
Esta función convierte una fecha en un número (el número de días desde el inicio de los tiempos).

### DATE (¡¡con comillas simples!!)
Es muy flexible: si le das una fecha fija como primer argumento, las modificaciones (como +15 days) se aplicarán sobre esa fecha en lugar de sobre el día de hoy.   
Cuando usas DATE('2026-04-05', '+15 days'), el motor hace el cálculo matemático del calendario por ti:   
Toma el 5 de abril.   
Le suma 15 días.   
El resultado que se grabará en la columna fecha_devolucion_prevista será automáticamente '2026-04-20'.

Ayer: `DATE('now', '-1 day')`

Antesdeayer: `DATE('now''-2 days')`

Ayer + 15 días: `DATE('now', '-1 day', '+15 days')` (que es lo mismo que +14 days).