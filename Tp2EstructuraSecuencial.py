import math

#Desarrollar un programa que permita ingresar dos números enteros A y
#B a través del teclado. Imprimir su suma y su diferencia.
def sumEnteros():
    a = int(input('Ingrese el primer numero entero '))
    b = int(input('Ingrese el segundo numero entero '))
    print('La suma de',a,'+',b,'es igual a',a+b,'.','La difencia entre',a,'y',b,'es de',a-b,'\n')

#Ingresar la longitud del radio de un círculo. Calcular e imprimir:
#· La superficie del círculo (Sup = pi * r²)
#· El perímetro de la circunferencia (Per = pi * d)
#· La superficie de la esfera (Sup = 4 * pi * r²)
#· El volumen de la esfera (Vol = 4/3 * pi * r³)
def supCirculo():
    radio = float(input('Ingrese el radio del circulo a calcular '))
    print('La superficie del círculo es de',math.pi*radio**2)
    print('El perímetro de la circunferencia es de',math.pi*radio*2)
    print('La superficie de la esfera es de',4*math.pi*radio**2)
    print('El volumen de la esfera es de',4/3*math.pi*radio**3,'\n')

#Escribir un programa que permita ingresar la edad de una persona en
#años y la convierta a días, imprimiendo el resultado. Considerar que todos
#los años tienen 365 días.
def calcEdad():
    edad = int(input('Ingrese edad '))
    print('Esta persona vivio',edad*365,'dias','\n')

#Leer una medida en metros e imprimir esta medida expresada en centímetros,
#pulgadas, pies y yardas. Los factores de conversión son:
#· 1 pie = 12 pulgadas
#· 1 yarda = 3 pies
#· 1 pulgada = 2,54 cm.
#· 1 metro = 100 cm.
def medidas():
    medida = float(input('Ingrese la medida en metros '))
    medida *= 100
    print('son',medida,'cm')
    medida /= 2.54
    print('son',medida,'pulgadas')
    medida /= 12 
    print('son',medida,'pies')
    medida /= 3
    print('son',medida,'yardas','\n')

#Ingresar tres números enteros, calcular su promedio y mostrarlo por
#pantalla.
def promedio():
    n1 = int(input('Ingrese el primer numero entero '))
    n2 = int(input('Ingrese el segundo numero entero '))
    n3 = int(input('Ingrese el tercer numero entero '))
    print('El promedio es',(n1+n2+n3)/3,'\n')

#Leer un período en segundos e imprimirlo expresado en días, horas, minutos
#y segundos. Por ejemplo, 200000 segundos equivalen a 2 días, 7
#horas, 33 minutos y 20 segundos.
def segundosCalc():
    tiempo = float(input('Ingrese el tiempo en segundos '))
    resultado = tiempo // 86400
    tiempo = tiempo % 86400
    print('son',resultado,'dias')

    resultado = tiempo // 3600 
    tiempo = tiempo % 3600
    print('son',resultado,'horas')

    resultado = tiempo // 60 
    tiempo = tiempo % 60
    print('son',resultado,'minutos')
    print('son',tiempo,'segundos','\n')

#Una inmobiliaria paga a sus vendedores un salario de $800, más una
#comisión de $50 por cada venta realizada, más el 5% del valor de esas
#ventas. Realizar un programa que imprima el número del vendedor y el
#salario que le corresponde en un determinado mes. Se leen el número
#del vendedor, la cantidad de ventas que realizó y el valor total de las
#mismas.
def inmobiliaria():
    nroVendedor = int(input('Ingrese el numero de vendedor '))
    cdadVentas = int(input('Ingrese la cantidad de ventas realizadas '))
    totVentas = float(input('Ingrese el valor total de las ventas '))
    print('El vendedor',nroVendedor,'ganara este mes',800+50*cdadVentas+0.05*totVentas,'\n')

#Un banco necesita para sus cajeros automáticos un programa que lea
#una cantidad de dinero e imprima a cuántos billetes equivale, considerando
#que existen billetes de $100, $50, $10, $5 y $1. Desarrollar dicho
#programa de tal forma que se minimice la cantidad de billetes entregados
#por el cajero.
def calcBilletes():
    cdadDinero = int(input('Ingrese el total de dinero '))
    b100 = cdadDinero // 100
    cdadDinero = cdadDinero % 100
    b50 = cdadDinero // 50
    cdadDinero = cdadDinero % 50
    b10 = cdadDinero // 10
    cdadDinero = cdadDinero % 10
    b5 = cdadDinero // 5
    cdadDinero = cdadDinero % 5
    print('El total ingresado equivale a',b100,'de $100',b50,'de $50',b10,'de $10',b5,'de $5',cdadDinero,'de $1','\n')

#Desarrollar un programa que solicite una temperatura expresada en grados
#centígrados y la imprima convertida a grados Fahrenheit, tal que:
# °C=5/9*(°F-32)
def calcTemp():
    gradosC = float(input('Ingrese temperatura en grados centigrados '))
    print('Son',gradosC /(5/9)+32,'grados Fahrenheit','\n')

#Escribir un programa para convertir un número binario de 4 cifras en un
#número decimal. El número binario se ingresa como un solo número entero
#de cuatro dígitos.
def convBinario():
    bi = int(input('Ingrese binario de 4 digitos '))
    dec = (bi % 10)
    bi = bi//10
    dec = dec +(bi % 10) * 2
    bi = bi//10
    dec = dec + (bi % 10) * 4
    bi = bi//10
    dec = dec + (bi % 10) * 8
    print ('Convertido a decimal es',dec)
print('Ingrese la operacion que desea realizar \n1 - Suma de enteros \n2 - Calcular circulo y esfera a partir del radio ')
print('3 - Calcular edad en días a partir de años\n4 - Conversor de medidas a partir de metros')
print('5 - Calcular promedio de tres números \n6 - Convertir sengudos a AA DD HH MM SS ')
print('7 - Calcular sueldo de vendedor de inmobiliaria \n8 - Calcular mínima cantidad de billetes a partir de un monto')
print('9 - Conversor de grados centigrados a farenheit \n10 - Conversor de número binario de 4 digitos a decimal')

select = int(input())

if(select == 1):
    sumEnteros()
elif(select == 2):
    supCirculo()
elif(select == 3):
    calcEdad()
elif(select == 4):
    medidas()
elif(select == 5):
    promedio()
elif(select == 6):
    segundosCalc()
elif(select == 7):
    inmobiliaria()
elif(select == 8):
    calcBilletes()
elif(select == 9):
    calcTemp()
elif(select == 10):
    convBinario()
else:
    print("Valor incorrecto, vuelva a intentar")







