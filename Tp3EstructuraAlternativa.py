
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




#Ejercicio 1: Ingresar dos números A y B e imprimir el mayor, o cualquiera si son iguales.
def ej1():
    a = float(input("Ingrese un numero"))
    b = float(input("Ingrese un numero"))
    if(a>b):
        print(a)
    elif(b>a):
        print(b)
    else:
        print(a)
        
#Ejercicio 2: Leer un número entero A e imprimir un mensaje indicando si es par o impar.
def ej2():
    a = int(input("Ingrese un numero"))
    if(a%2==0):
        print('Par')
    else:
        print('Impar')
        
#Ejercicio 3: Leer un número entero N y determinar si es un número natural (positivo y distinto
#de 0). Si lo es, imprimirlo junto con su doble. En caso contrario, imprimirlo
#junto con su triple.
def ej3():
    n = int(input('Ingrese un numero entero '))
    if n>0:
        print(n,n*2)
    else:
        print(n,n*3)

#Ejercicio 4: Ingresar dos números enteros A y B. Desarrollar un programa que determine si
#A es múltiplo de B y si B es múltiplo de A. Imprimir mensajes aclaratorios.
def ej4():
    a = float(input("Ingrese un numero"))
    b = float(input("Ingrese un numero"))
    if(a%b==0):
        print('A es multiplo de B')
    else:
        print('A no es multiplo de B')
    if(b%a==0):
        print('B es multiplo de A')
    else:
        print('B no es multiplo de A')

#Ejercicio 5: Desarrollar un programa para leer la base y la altura de un triángulo e imprimir
#su superficie. El algoritmo debe validar los datos de entrada, verificando que
#éstos sean números positivos. En caso contrario debe imprimirse el dato erróneo
#junto con una leyenda aclaratoria. Se recuerda que Sup = (Base * Altura) / 2.
def ej5():
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

#Ejercicio 6: Una editorial determina el precio de un libro según la cantidad de páginas que
#contiene. El costo básico del libro es de $125, más $2,20 por página con encuadernación
#rústica. Si el número de páginas supera las 300 la encuadernación
#debe ser en tela, lo que incrementa el costo en $80. Además, si el número de
#páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación
#que incrementa el costo en $136. Desarrollar un programa que
#calcule el costo de un libro dado el número de páginas.
def ej6():
    paginas = int(input('Ingrese la cantidad de paginas del libro a imprimir'))
    costo = 125 + 2.2 * paginas
    if(paginas > 600):
        costo += 80+136
    elif(paginas >300):
        costo += 80
    print('El costo de imprimir el libro es de',costo)

#Ejercicio 7: Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
#· Aplica el precio base a la primera docena de unidades.
#· Aplica un 10% de descuento a todas las unidades entre 13 y 100.
#· Aplica un 25% de descuento a todas las unidades por encima de las 100.
#Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio
#base es 100. El cálculo resultante sería:
#100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
#Desarrollar un programa que lea la cantidad solicitada de un producto y su precio
#base, e imprima el valor total de la venta y el precio promedio.
def ej7():
    cant=int(input('Ingrese la cantidad de productos a comprar'))
    pBase=float(input('Ingrese el precio base del producto'))
    total = 0
    if(cant>100):
        total = (cant - 100) * (pBase-pBase*0.25)
    
    

#Ejercicio 8: Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga
#su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento
#de $120 o del 2% de la factura, lo que resulte menor. Si paga en los siguientes
#10 días del mes deberá pagar el importe original de la factura, mientras que si
#paga después del día 20 deberá abonar una multa de $150 o del 10% de su factura,
#lo que resulte mayor. Desarrolle un programa que lea el número del cliente
#y el total de la factura, y emita un informe donde conste el número del cliente y
#los tres importes que podrá abonar según la fecha de pago.

#Ejercicio 9: Leer un número correspondiente a un año e imprimir un mensaje indicando si es
#bisiesto o no. Se recuerda que un año es bisiesto cuando es divisible por 4. Sin
#embargo, aquellos años que sean divisibles por 4 y también por 100 no son bisiestos,
#a menos que también sean divisibles por 400. Por ejemplo, 1900 no fue
#bisiesto pero sí el 2000.

#Ejercicio 10: Desarrollar un programa para leer las longitudes de los tres lados de un triángulo
#L1, L2, L3 y determinar qué tipo de triángulo es según la siguiente clasificación:
#· Si A >= B + C no se trata de un triángulo.
#· Si A² = B² + C² se trata de un triángulo rectángulo.
#· Si A² > B² + C² se trata de un triángulo obtusángulo.
#· Si A² < B² + C² se trata de un triángulo acutángulo.
#Tener en cuenta que A denota el mayor de los lados L1, L2 y L3, mientras que B
#y C corresponden a los dos lados restantes.

#Ejercicio 11: La fecha de Pascua para un año cualquiera X puede determinarse mediante el
#siguiente algoritmo:
#· Calcular el resto de dividir X sobre 19 y llamarlo A.
#· Calcular el resto de dividir X sobre 4 y llamarlo B.
#· Calcular el resto de dividir X sobre 7 y llamarlo C.
#· Multiplicar A por 19, sumarle 24 y calcular el resto de dividir este resultado
#por 30. Este resto recibirá el nombre D.
#· Multiplicar B por 2, C por 4 y D por 6. Sumar los tres resultados y sumarle
#5. Calcular el resto de dividir este último resultado por 7 y llamarlo E.
#· La fecha de Pascua se obtiene sumando los valores D y E, más la constante
#22.
#· El resultado se expresa como una fecha dentro del mes de Marzo. Si el
#número es mayor que 31, entonces ese año Pascua se celebrará en el
#mes de Abril. Ejemplo: Un resultado 35 significa que Pascua cae el 4 de
#Abril (35 menos los 31 días del mes de Marzo es igual a 4).
#Preparar un programa que permita ingresar el año y calcule la fecha de Pascua.

#Ejercicio 12: Leer tres números correspondientes al día, mes y año de una fecha e imprimir
#un mensaje indicando si la fecha es válida o no.

#Ejercicio 13: Diseñar un programa que calcule y muestre el sueldo neto de un empleado en
#base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
#el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es
#casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
#También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social: 3%, Sindicato: 3%
#Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad
#y estado civil (‘s’ o ‘c’). Se debe informar: (reemplazar los 9 por los
#valores que correspondan)
#Estado Civil: Soltero/Casado
#Sueldo básico Antigüedad Descuentos Importe
#$ 999.99 99 años + 999.99
#Jubilación - 999,99
#Obra Social - 999,99
#Sindicato - 999,99
#------------
#Sueldo Neto 999,99





















