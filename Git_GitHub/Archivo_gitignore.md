**Crear archivo `.gitignore`**

Debemos indicar el tipo de archivos que queremos pasar a `.gitignore` antes de hacer commit,   

- echo ".DS_Store" > .gitignore  # macOS
- echo "Thumbs.db" >> .gitignore  # Windows
- echo "*.tmp" >> .gitignore  # Archivos temporales
- git add .gitignore
- git commit -m "chore: añadir gitignore"
- git push


```
# Python
__pycache__/
*.pyc
.venv/
.env

# Datos sensibles
*.csv
*.xlsx
credenciales.json

# Sistema
.DS_Store
Thumbs.db
```