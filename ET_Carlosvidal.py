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
    encontrados[]
    total = 0
    for codigo, datos in bodega.items():
        if datos[1].lower() == categoria.lower():
            total += bodega[codigo][1]
    print ("El total de ") 

def busqueda_precio(categoria, prendas, bodega): 