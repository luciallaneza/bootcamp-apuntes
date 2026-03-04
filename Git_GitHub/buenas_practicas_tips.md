## 🎯 Buenas Prácticas

### Mensajes de commit
```bash
# ✅ Buenos mensajes
git commit -m "feat: añadir función de login"
git commit -m "fix: corregir error en cálculo de promedio"
git commit -m "docs: actualizar README con instrucciones"

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