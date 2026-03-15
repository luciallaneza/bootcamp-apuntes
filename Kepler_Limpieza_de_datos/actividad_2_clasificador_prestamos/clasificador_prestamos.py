
def clasificar_prestamo(dias):
    if dias <= 21:
        return{"estado":"A Tiempo", "penalizacion" : 0.00}
    elif dias <= 30:
        dias_extra = dias - 21
        return{"estado" :"Retraso leve", "penalizacion" : dias_extra * 0.50}
    else:
        dias_extra = dias - 30
        return{"estado" : "Retraso grave", "penalizacion" : dias_extra * 1.00}

prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]
for dias in prestamos_dias:
    print(dias, clasificar_prestamo(dias)["estado"], clasificar_prestamo(dias)["penalizacion"])