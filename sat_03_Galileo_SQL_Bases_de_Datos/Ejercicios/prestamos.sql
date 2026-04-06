-- Crear tabla de préstamos
CREATE TABLE prestamos (
    id INTEGER PRIMARY KEY,
    usuario TEXT,
    libro TEXT,
    dias_prestamo INTEGER,
    categoria TEXT
);

INSERT INTO prestamos (usuario, libro, dias_prestamo, categoria) VALUES
('Ana', '1984', 15, 'Ficción'),
('Carlos', 'Sapiens', 22, 'Ensayo'),
('María', 'Watchmen', 18, 'Cómic'),
('Ana', 'El Quijote', 30, 'Ficción'),
('Luis', 'Batman', 12, 'Cómic'),
('Carlos', '1984', 25, 'Ficción');

-- Seleccionar todos los préstamos de Ana
SELECT * FROM prestamos
	WHERE usuario = "Ana";

-- Préstamos de más de 20 días
SELECT * FROM prestamos
	WHERE dias_prestamo > 20;

-- Préstamos de ficción o cómic, ordenados por días, descendente
SELECT * FROM prestamos
	WHERE categoria IN ("Ficción","Cómic")
	ORDER BY dias_prestamo DESC; 

-- Los tres préstamos más largos
SELECT * FROM prestamos
	ORDER BY dias_prestamo DESC
	LIMIT 3;
	
-- Categorías únicas
SELECT DISTINCT categoria FROM prestamos;
	