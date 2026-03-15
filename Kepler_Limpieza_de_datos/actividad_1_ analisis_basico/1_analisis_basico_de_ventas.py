# Datos
enero = 4500
febrero = 5200
marzo = 4800
abril = 5150
mayo = 4300
junio = 4950
julio = 4700
agosto = 4600
septiembre = 5080
octubre = 4990
noviembre = 5020
diciembre = 4700
meta_anual = 50000


total_ventas = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre + diciembre # variable que indiciqe omo calcular el total de las ventas
print("El total de las ventas son ", total_ventas, "Euros")

promedio = total_ventas / 12 # cálculo del promedio
print("El promedio de las ventas es ", promedio)

# 3.Identifique el mes con mayores ventas
mayores_ventas = max (enero,febrero,marzo,abril,mayo,junio, julio, agosto, septiembre, octubre, noviembre, diciembre)
print("El mes con mayor venta es ", mayores_ventas)

# 4 . Determine si se alcanzó la meta anual (50000)
bonus = total_ventas - meta_anual
if total_ventas >= meta_anual:
      print("Se ha logrado la meta anual, se ha superado en ", bonus)
else:
    print("Este año no se han conseguido objetivos, han faltado ", bonus)