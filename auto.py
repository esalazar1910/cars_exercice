#<<< PARTE I >>>
#Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarseles:
#Nombre y Apellido del comprador, Marca, Puertas y Color
#Marcas Posibles y sus precios
#Ford: $100000
#Chevrolet: $120000
#Fiat: $80000
#Por la cantidad de puertas se añade al precio:
#2 Puertas: $50000
#4 Puertas: $65000
#5 Puertas: $78000
#Dependiendo del color debe sumar:
#Blanco: $10000
#Azul: $20000
#Negro: $30000
#Se debe imprimir los datos de cada comprador y el precio total

#<<< PARTE II >>>
#1. El programa debe preguntar cuantos usuarios se les va a vender, dependiendo de la respuesta
#se ejecutará tantas veces la parte I
#2. Si el pedido no es un auto en venta, se debe repetir la pregunta, lo mismo con los colores y puertas
#3. Al final de todo se debe preguntar si hay más clientes que ingresar, si la respuesta es afirmativa
#comenzará todo el proceso nuevamente
#4. Aplicar estos descuentos si el precio final supera:
#150 mil - 10%
#200 mil - 15%
#220 mil - 18%
#5. Solo se mostrará que se vendió al final del programa

marcas = ({'FORD': 100000, 'CHEVROLET':120000, 'FIAT': 80000})
puertas = ({2: 50000, 4: 65000, 5: 78000})
colores = ({'BLANCO': 10000, 'AZUL': 20000, 'NEGRO': 30000})
decisiones = 'SI'
resultados = []

def precio_total(pre_marca, pre_puerta, pre_color):
    precio_final = pre_marca + pre_puerta + pre_color
    if(precio_final >= 220000):
        precio_total = precio_final * 0.82
        return precio_total
    elif(precio_final >= 200000):
        precio_total = precio_final * 0.85
        return precio_total
    elif(precio_final >= 150000):
        precio_total = precio_final * 0.90
        return precio_total
    else:
        return precio_final

def registro(num_ventas):
    for num in range(num_ventas):
        nombre = input('Ingresa el nombre del comprador: ')
        apellido = input('Ingresa el apellido del comprador: ')
        marca = ''
        while marca not in marcas.keys():
            marca = input('Ingresa la marca que quiere el comprador: ')
            marca = marca.upper()
        puerta = 0
        while puerta not in puertas.keys():
            puerta = int(input('Ingresar la cantidad de puertas que quiere el comprador: '))
        color = ''
        while color not in colores.keys():
            color = input('Ingresa el color de auto que quiere el comprador: ')
            color = color.upper()
        pre_marca = marcas[marca]
        pre_puerta = puertas[puerta]
        pre_color = colores[color]
        pre_final = precio_total(pre_marca, pre_puerta, pre_color)
        cliente = {'id': num, 'nombre' : nombre, 'apellido': apellido, 'marca': marca, 'puertas': puerta, 'color': color, 'total': pre_final}
        resultados.append(cliente)

def print_final(resultados):
    for num in resultados:
        print('La venta número', num['id'], 'fue realizada por', num['nombre'], num['apellido'], 
        ', compro un auto', num['marca'], 'con', num['puertas'], 'puertas y de color', 
        num['color'], 'el total de su compra fue de', num['total'])
    

while decisiones == 'SI':
    num_ventas = int(input('¿Cuantas ventas quieres registrar? ' ))
    registro(num_ventas)
    decisiones = input('¿Quieres ingresar más ventas: ')
    decisiones = decisiones.upper()
    if(decisiones == 'NO'):
        print_final(resultados)
