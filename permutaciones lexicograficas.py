#Función para obtener  el factorial de un número
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

#Función para recuperar la posición de la permutación lexicografica de una cadena ingresada
#Ingresamos la cadena y el número de permutación solicitada
def permutacion(cadena, pos):
    #La cantidad de permutaciones lineales es igual al factorial de la cantidad de caracteres de la cadena
    cantidadPermutaciones = factorial(len(cadena))

    #El indice lo usaremos para ir buscando en bloques
    #Si fueran 3 letras, la cantidad serñia 6, y el indice iria de 2 en 2 para la primera letra
    #2 'A's, 2'B's y 2 'C's -> ABC, ACB, BAC, BCA, CAB, CBA
    Indice = cantidadPermutaciones
    
    #La posicion la iremos moviendo en bloques cada vez más pequeños
    #hasta llegar a movernos de 1 en 1 y encontrar la posición adecuada
    posUbicada = 0

    #Letra es la posicion de la letra que estamos buscando en ese momento
    #irá desde 0 hasta la longitud de la cadena
    letra = 0

    #Este es el arreglo que iremos formando, y luego lo convertiremos en cadena
    permutacion=[]
    CadenaFinal=""
    
    #Creamos esta cadena auxiliar porque la cadena principal irá cambiando dinámicamente
    cadenaAux = cadena

    #Bucle hasta que completemos las letras ubicadas
    while letra<len(cadenaAux): #OR posUbicada == pos
        #Como dijimos, el bloque inicial será la cantidad de permutaciones entre la cantidad de
        #opciones disponibles, como la cadena está intacta, las opciones son la cantidad de letras
        Indice/=len(cadena)

        #Bucle para comparar el bloque con la posicion buscada, mientras sea menor se asigna
        #Si es mayor ya se ignora, coloco pos-1 porque el usuario usa números de 1 a más,
        #pero en lógica se usa desde el 0
        for i in range(len(cadena)):
            if Indice*i<=(pos-1)-posUbicada:
                letraElegida = cadena[i]
                IndiceAux = Indice*i
            else:
                break;
        #Guardamos la letra elegida
        permutacion.append(letraElegida)
        #Nuestra posicion ubicada ahora está más cerca de la buscada pero desde abajo, osea es menor
        posUbicada+=IndiceAux
        #Quitamos la letra que ya usamos de la cadena
        cadena = cadena.replace(letraElegida,'')
        #Pasamos a la siguiente letra
        letra+=1

    #Una vez finalizado el proceso, juntaremos las letras en un arreglo
    for letra in permutacion:
        CadenaFinal+=letra

    return CadenaFinal

cadena = input("Ingrese la cadena que desea permutar: ")
numero = int(input("Qué número de permutacion desea obtener?: "))

print(permutacion(cadena,numero))

