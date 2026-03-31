# Estructura básica de una consulta SQL

```sql
SELECT columnas          -- Qué quieres ver
FROM tabla              -- De dónde
WHERE condiciones       -- Filtros
ORDER BY columna        -- Orden
LIMIT cantidad;         -- Cuántas filas máximo
```

Cada parte es opcional excepto `SELECT` y `FROM`.

# 🔍 SQL Básico: SELECT, WHERE, ORDER BY

## SELECT: La consulta fundamental

`SELECT` es cómo pides datos a una base de datos.

### Seleccionar todo

```sql
SELECT * FROM libros;
```

`*` significa "todas las columnas".

### Seleccionar columnas específicas

```sql
SELECT titulo, autor FROM libros;
```

Solo ves las columnas que necesitas.

### Renombrar columnas en el resultado (alias)

```sql
SELECT 
    titulo AS libro,
    autor AS escritor
FROM libros;
```

Útil para resultados más legibles.

## WHERE: Filtrar resultados

`WHERE` filtra filas según condiciones.

### Operadores de comparación

| Operador | Significado |
|----------|-------------|
| `=` | Igual |
| `!=` o `<>` | Diferente |
| `>` | Mayor |
| `<` | Menor |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

### Condiciones múltiples

**AND** - Ambas condiciones deben cumplirse   
**OR** - Al menos una condición debe cumplirse   
**Combinar AND y OR** (usa paréntesis):

```sql
SELECT * FROM libros
WHERE (categoria = 'Ficción' OR categoria = 'Ensayo')
  AND año > 2000;
```

### Operadores especiales

**IN** - Verifica si está en una lista   
**BETWEEN** - Rango de valores   
**LIKE** - Búsqueda de patrones en texto    
```sql
-- Libros cuyo título empieza con "El"
SELECT * FROM libros
WHERE titulo LIKE 'El%';

-- Libros que contienen "amor" en el título
SELECT * FROM libros
WHERE titulo LIKE '%amor%';

-- % = cualquier cantidad de caracteres
-- _ = exactamente un carácter
```
**IS NULL** - Valores nulos    
**ORDER BY**: Ordenar resultados (Orden ascendente por defecto, podemos poner DESC)    
**LIMIT**: Limita resultados   
**DISTINCT**: Elimina duplicados   


## HAVING: Filtrar grupos

`WHERE` filtra filas **antes** de agrupar.  
`HAVING` filtra grupos **después** de agregar.

### Diferencia entre WHERE y HAVING

```sql
-- WHERE: Filtra filas individuales
SELECT categoria, COUNT(*) 
FROM prestamos
WHERE dias_prestamo > 15  -- Solo cuenta préstamos > 15 días
GROUP BY categoria;

-- HAVING: Filtra grupos
SELECT categoria, COUNT(*) AS total
FROM prestamos
GROUP BY categoria
HAVING COUNT(*) > 1;  -- Solo muestra categorías con más de 1 préstamo
```

### Ejemplo combinado

```sql
-- Categorías con más de 1 préstamo, excluyendo préstamos cortos
SELECT 
    categoria,
    COUNT(*) AS total,
    AVG(dias_prestamo) AS promedio
FROM prestamos
WHERE dias_prestamo > 10  -- Filtra filas
GROUP BY categoria
HAVING COUNT(*) > 1;  -- Filtra grupos
```

Se recomienda hacer un backup de la tabla antes de borrar:
CREATE TABLE backup_nombre_tabla AS
SELECT * FROM nombre_tabla;

## Regla de oro

**Si usas una función de agregación (COUNT, SUM, AVG, MIN, MAX):**
- Todas las columnas que NO estén dentro de una función de agregación
- DEBEN estar en el GROUP BY

```sql
-- ✅ Correcto
SELECT categoria, COUNT(*)
FROM prestamos
GROUP BY categoria;

-- ✅ Correcto
SELECT usuario, categoria, COUNT(*)
FROM prestamos
GROUP BY usuario, categoria;

-- ❌ Incorrecto (falta categoria en GROUP BY)
SELECT usuario, categoria, COUNT(*)
FROM prestamos
GROUP BY usuario;