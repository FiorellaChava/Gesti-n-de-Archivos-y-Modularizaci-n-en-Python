# Proyecto: fiorella proyecto
# Estudiante: fiorella chavarria
# Fecha de Inicio: 2/4/2025
# Fecha de Entrega: 2/4/2025
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

from analisis_datos import *

lista_compras = generar_lista_de_compras()
print(lista_compras)
precios = [precio for _, precio in lista_compras]
print('Media: ', media(precios))
print('Mediana: ', calcular_mediana(precios)) 