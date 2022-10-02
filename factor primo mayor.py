import math

def divisoresN(numero):
    raiz = round(math.sqrt(numero))
    divisores=[]
    for i in range(raiz):
            if numero%(i+1)==0:
                divisores.append((i+1))
                if (i+1) != int(numero/(i+1)):
                    divisores.append(int(numero/(i+1)))
    return divisores

def EsPrimo(numero):
    if len(divisoresN(numero))>2:
        return False
    else:
        return True


def mayor(numeros):
    mayor=0
    for n in numeros:
        if n>mayor:
            mayor=n
    return mayor

def factorPrimoMayor(numero):
    divisores = divisoresN(numero)
    divisoresPrimos = []

    for divisor in divisores:
        if EsPrimo(divisor):
            divisoresPrimos.append(divisor)

    mayorFactPrimo = mayor(divisoresPrimos)

    return mayorFactPrimo


numero = int(input("De qué número desea conocer su mayor factor primo ?: "))

print("El mayor factor primo de ", numero, " es: ", factorPrimoMayor(numero))
