#Leer un número entero N y determinar si es un número natural
#(positivo y distinto de 0). Si lo es, imprimirlo junto con su doble.
#En caso contrario, imprimirlo junto con su triple.

n = int(input('Ingrese un numero entero '))
if n>0:
    print(n,n*2)
else:
    print(n,n*3)

#Desarrollar un programa para leer la base y la altura de un triángulo e imprimir
#su superficie. El algoritmo debe validar los datos de entrada, verificando que
#éstos sean números positivos. En caso contrario debe imprimirse el dato erróneo
#junto con una leyenda aclaratoria. Se recuerda que Sup = (Base * Altura) / 2.

base = float(input('Ingrese la base '))
altura = float(input('Ingrese la altura '))
if(base<=0 and altura<=0):
    print("Error en los dos datos")
else:
    if base<=0:
        print("Error al ingresar la base")
    elif altura<=0:
        print("Error al ingresar la altura")
    else:
        print("La superficie es",(base*altura)/2)

#Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga
#su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento
#de $120 o del 2% de la factura, lo que resulte menor. Si paga en los siguientes
#10 días del mes deberá pagar el importe original de la factura, mientras que si
#paga después del día 20 deberá abonar una multa de $150 o del 10% de su factura,
#lo que resulte mayor. Desarrolle un programa que lea el número del cliente
#y el total de la factura, y emita un informe donde conste el número del cliente y
#los tres importes que podrá abonar según la fecha de pago.

nCliente = int(input('Ingrese el numero de cliente'))
tFactura = float(input('Ingrese el total de la factura'))

print("El cliente numero",nCliente,"Debera abonar")

if tFactura * 0.02 < 120:
    total = tFactura - tFactura *0.02
else:
    total = tFactura - 120
print("Si paga del 1 al 10",total)
print("Si paga del 11 al 20",tFactura)
if tFactura * 0.1 > 150:
    total = tFactura + tFactura *0.1
else:
    total = tFactura + 150
print("Si paga del 21 en adelante",total)




























