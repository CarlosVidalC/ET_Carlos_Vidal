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

def validar_unisex(es_unisex):
    return es_unisex.lower() in ("s", "n")

def validar_precio(precio):
    try:
        return int(precio) > 0 
    except ValueError:
        return False

def validar_unidades(unidades):
    try:
        return int(unidades) >= 0 
    except ValueError: 
        return False

def agregar_prenda(codigo, nombre, categoria, talla,color, material, es_unisex, precio, unidades, prendas,bodega):
    if buscar_codigo(codigo,prendas):
        return False
    else:
        prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex]
        bodega[codigo] = [precio, unidades]
        return True

def eliminar_prenda(codigo, prendas,bodega):
    if buscar_codigo(codigo, prendas):
        del prendas[codigo]
        del bodega[codigo]
        return True
    else: 
        return False

def mostrar_menu(): 
    print(''' ========== MENÚ PRINCIPAL ==========
        1. Unidades por categoría
        2. Búsqueda de prendas por rango de precio
        3. Actualizar precio de prenda
        4. Agregar prenda
        5. Eliminar prenda
        6. Salir
        =====================================''')

def opcion_1(prendas, bodega):
    categoria = input("Ingrese categoria a consultar:")    
    unidades_categoria(categoria,prendas,bodega)

def opcion_2(prendas,bodega):
    precio_minimo = 0 
    precio_maximo = 0
    datos_validos = False
    while not datos_validos:
        try:
            precio_minimo = int("Ingrese precio mínimo: ")
            precio_maximo = int("Ingrese precio máximo: ")
            if precio_minimo <= 0 and precio_maximo >= precio_minimo:
                return True
            else: 
                print ("Debe ingresar valores enteros.")
        except ValueError: 
            print ("Debe ingresar valores enteros.")
    busqueda_precio(precio_minimo, precio_maximo, prendas, bodega)

def opcion_3(bodega):
    continuar = True
    while continuar:
        codigo = input("Ingrese el codigo de la prenda: ").strip().lower()
        precio_valido = True
        nuevo_precio = 0
        while not precio_valido:
            try: 
                nuevo_precio = int(input("Ingrese el nuevo precio de la prenda: "))
                if nuevo_precio > 0: 
                    precio_valido = True
                else: 
                    print("El precio debe ser un entero mayor que cero.")
            except ValueError: 
                print ("El precio debe ser un entero mayor que cero.")

        if actualizar_precio(codigo, nuevo_precio,bodega):
            print ("Precio actualizado")
        else: 
            print ("El código no existe.")

        respuesta = input ("Desea actualizar otro precio (s/n): ")
        if respuesta == "s":
            continue 
        else: 
            break
                    
def opcion_4:

