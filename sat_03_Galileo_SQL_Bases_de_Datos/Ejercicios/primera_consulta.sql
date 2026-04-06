CREATE TABLE libros (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    autor TEXT,
    categoria TEXT,
    año INTEGER
);

INSERT INTO libros (titulo, autor, categoria, año) 
VALUES ('1984', 'George Orwell', 'Ficción', 1949);

INSERT INTO libros (titulo, autor, categoria, año) 
VALUES ('Sapiens', 'Yuval Harari', 'Ensayo', 2011);

SELECT * FROM libros;