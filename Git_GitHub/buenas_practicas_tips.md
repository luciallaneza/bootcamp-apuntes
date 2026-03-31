## 🎯 Buenas Prácticas

### Mensajes de commit
```bash
# ✅ Buenos mensajes
git commit -m "feat:  " --> para añadir función de login, una nueva ccaracterística para el usuario.
git commit -m "fix:   " --> para corregir un error, arreglar un bug que afecta al usuario.
git commit -m "docs:  " --> cambios en la documentación.
git commit -m "perf:  " --> cambios que mejoran el rendimiento del sitio.
git commit -m "build: " --> cambios en el sistema de build, tareas de despliegue o instalación.
git commit -m "ci:    " --> cambios en la integración continua.
git commit -m "style: " --> cambios de formato, tabulaciones, espacios o puntos y coma, etc; no afectan al usuario.
git commit -m "refactor:  " --> refactorización del código como cambios de nombre de variables o funciones.
git commit -m "test:  " --> añade tests o refactoriza uno existente.


# ❌ Malos mensajes
git commit -m "cambios"
git commit -m "fix"
git commit -m "asdfasdf"
```
---

### ✨ Tips Rápidos

```bash
# Ver cambios antes de commit
git diff

# Deshacer último commit (mantiene cambios)
git reset --soft HEAD~1

# Ver historial bonito
git log --oneline --graph --all --decorate

# Crear alias útiles
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
```