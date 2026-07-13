prendas = {
'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon',
True],
'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester',
True],
'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon',
True],
'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon',
False],
}

bodega = {
'S001': [7990, 12],
'S002': [19990, 0],
'S003': [29990, 3],
'S004': [24990, 6],
'S005': [17990, 8],
'S006': [14990, 2],
}

def leer_opcion():
    opcion = 0 
    opcion_valida = False
    while not opcion_valida: 
        try: 
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <=6: 
                opcion_valida = True
            else:
                print("Error.")
        except ValueError: 
            print("Error.")
    return opcion

def unidades_categoria(categoria, prendas, bodega):
    total = 0
    for codigo, datos in bodega.items():
        if datos[1].lower() == categoria.lower():
            total += bodega[codigo][1]
    print ("El total de ") 

def busqueda_precio(precio_minimo, precio_maximo, prendas, bodega):
    encontrados[]
    for codigo, datos in bodega.items():
        precio = datos [0]
        unidades = datos [1]
        if precio_minimo <= precio <= precio_maximo and unidades != 0:
            nombre = prendas[codigo][0]
            encontrados.append(f"{nombre}--{codigo}")
    
    encontrados.sort()

    if len(encontrados) == 0:
        print ("No hay prendas en ese rango de precio.")
    else: 
        print (f"Las prendas encontradas son: {encontrados}")

def buscar_codigo(codigo, prendas(diccionario)):
    return codigo in diccionario

def actualizar_precio(codigo, nuevo_precio, bodega):
    if buscar_codigo(codigo, bodega):
        bodega[codigo][0] = nuevo_precio
        return True
    else:
        return False

def validar_texto(dato):
    return len(dato.strip()) > 0

