def alarma():
    total_alarmas = int(input('Cuantas alarmas desea agregar: '))
    start_range = 1
    while start_range <= total_alarmas:
        hora = str(input('Hora - Alarma ' + str(start_range) + ' :'))
        # if hora > 24:
        # if hora < 0:
        minuto = str(input('Minutos - Alarma ' + str(start_range) + ' :'))
        mensaje = str(input('Mensaje - Alarma ' + str(start_range) + ' :'))

        print('Son las ' + hora + ':' + minuto + ' horas')
        print(mensaje)

        print('----------   FIN DEL PROGRAMA   ----------')
        start_range += 1

    startapp()


# No entend  a lo que se refiere con cantidad de digitos
# puedo asumir que es a la suma de valores 202020 = 6  por que 2 + 0 + 2 + 0 + 2 + 0 = 6
# o se refieren al conteo de digitos 
def numeros():
    numero = int(input('Ingrese un número: '))
    lista = list(str(numero))
    suma_lista = 0
    for y in lista:
        suma_lista = suma_lista + int(y)

    if int(lista[0]) == 1:
        reversed = int(str(numero)[::-1])
        print(reversed)

    # elif int(lista[0]) % 2 == 0 & len(str(numero)) % 2 == 0:
    elif int(lista[0]) % 2 == 0 & suma_lista % 2 == 0:
        new_value = ''
        for x in range(0, len(lista)):
            if x % 2 == 0:
                new_value = new_value + lista[x]
        print(new_value)

    # elif int(lista[0]) % 2 == 1 & len(str(numero)) % 2 == 1:
    elif int(lista[0]) % 2 == 1 & suma_lista % 2 == 1:
        internet = int(len(lista)) / 2
        value_one = lista[0]
        value_two = lista[int(internet)]
        print(value_one + value_two)

    startapp()


def matematica():
    for value in range(1, 1000):
        lista = list(str(value))
        tamaño_lista = len(lista)
        x = 0
        total = 0
        while x < tamaño_lista:
            # print('X ES ', x)
            if x + 1 == tamaño_lista:
                # print('Ultimo digito')
                if (total == int(lista[x])):
                    print('EL NÚMERO ' + str(value) + ' ES H4X0R')

            # print('VALOR A SUMAR ', lista[x])
            total += int(lista[x])
            # print('LA SUMA ES', total)

            x += 1

    startapp()


def bodega():
    golosinas = ['galletas', 'chupetines', 'chicles']
    aseo = ['jabon', 'shampo', 'acondicionador']
    limpieza = ['lavavajillas', 'detergente', 'limpiador de piso']
    print('=========================================================')
    print('================ PRODUCTOS A REGISTRAR ==================')
    print('=========================================================')
    print('GOLOSINAS : Galletas, Chupetines y Chicles')
    print('ASEO PERSONAL : Jabon, Shampo y Acondicionador')
    print('LIMPIEZA : Lavavajillas, Detergente y Limpiador de piso')
    print('=========================================================')

    total = int(input('Cuantos productos desea registrar: '))
    golosina_name_list = []
    golosina_price_list = []
    golosina_cant_list = []

    aseo_name_list = []
    aseo_price_list = []
    aseo_cant_list = []

    limpieza_name_list = []
    limpieza_price_list = []
    limpieza_cant_list = []

    start = 1
    price_total = 0
    cant_total = 0
    cant_total_golosina, cant_total_aseo, cant_total_limpieza = 0, 0, 0
    while start <= total:
        name = str(input('Nombre del producto [' + str(start) + '] :')).lower()
        price = int(input('Precio unitario del producto [' + str(start) + '] :'))
        cant = int(input('Cantidad de productos [' + str(start) + '] :'))
        price_total = price_total + (cant * price)
        cant_total = cant_total + cant

        for value in golosinas:
            if value == name:
                print('golosina')
                golosina_name_list.append(name)
                golosina_price_list.append(price)
                golosina_cant_list.append(cant)
                cant_total_golosina = cant_total_golosina + cant

        for value in aseo:
            if value == name:
                print('aseo')
                aseo_name_list.append(name)
                aseo_price_list.append(price)
                aseo_cant_list.append(cant)
                cant_total_aseo = cant_total_aseo + cant

        for value in limpieza:
            if value == name:
                print('limpieza')
                limpieza_name_list.append(name)
                limpieza_price_list.append(price)
                limpieza_cant_list.append(cant)
                cant_total_limpieza = cant_total_limpieza + cant

        start += 1

    print('Precio total a pagar : ', price_total)
    print('Cantidad productos vendidos : ', cant_total)
    print('Porcentaje de cantidad productos de limpieza : ', (cant_total_limpieza * 100) / cant_total)
    print('Porcentaje de cantidad productos de aseo personal : ', (cant_total_aseo * 100) / cant_total)
    print('Porcentaje de cantidad golosinas : ', (cant_total_golosina * 100) / cant_total)

    startapp()


def startapp():
    print('=========================================================')
    print('================          MENU         ==================')
    print('=========================================================')
    print('1) Ejercicio 01')
    print('2) Ejercicio 02')
    print('3) Ejercicio 03')
    print('4) Ejercicio 04')
    print('=========================================================')
    print('Para salir ingrese 0')
    print('=========================================================')
    number = int(input('Ingrese numero:'))
    print('')

    if number == 1:
        print('=========================================================')
        print('EJERCICIO 01')
        print('=========================================================')
        alarma()
    elif number == 2:
        print('=========================================================')
        print('EJERCICIO 02')
        print('=========================================================')
        numeros()
    elif number == 3:
        print('=========================================================')
        print('EJERCICIO 03')
        print('=========================================================')
        matematica()
    elif number == 4:
        print('=========================================================')
        print('EJERCICIO 04')
        print('=========================================================')
        bodega()
    elif number == 0:
        exit()


if __name__ == '__main__':
    startapp()
