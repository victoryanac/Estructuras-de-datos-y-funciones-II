import sys

# lista de productos y sus precios
productos = {
    'Notebook': 50000,
    'Monitor': 40000,
    'Escritorio': 35000,
    'Tarjeta de Video': 45000,
    'Teclado': 25000,
    'Mouse': 15000,
}

#verifica la candidad de argumentos ingresados por el usuario
umbral_filtro = int(sys.argv[1])
citerio_filtro = sys.argv[2] if len(sys.argv) > 2 else 'mayor'

productos_filtrados = {} 
#criterios de filtro que ingresa en la variable productos_filtrados
if citerio_filtro == 'mayor':
    productos_filtrados = {nombre_producto:precio for nombre_producto, precio in productos.items() if precio > umbral_filtro}
elif citerio_filtro == 'menor':
    productos_filtrados = {nombre: precio for nombre, precio in productos.items() if precio < umbral_filtro}


#criterios de impresion
if productos_filtrados:
    print(f"Los productos {citerio_filtro}es al umbral son:", ', '.join(productos_filtrados.keys()))
else:
    print(f"No hay productos {citerio_filtro}es al umbral especificado.")


