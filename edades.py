def pares(number): #Number es un parametro que recibe la funcion 
    if number==0:
        return 'El 0 es un caso especial pero se considera como par'
    elif number % 2==0:
        return 'Es par'
    else:
        return 'Es impar'
    
print(pares(0))

def mul10(number):
    if number % 10==0:
        return 'Es multiplo de 10'
    else:
        'No es multiplo de 10'

def positivoOnegativo (number):
    if number==0:
        return 'El numero es cero'
    elif number>0:
        return 'EL numero es positivo'
    else:
        return 'El numero es negativo'
print(positivoOnegativo(8))

def sumando(numero1, numero2):
    resultado= numero1 + (numero2*25)
    return 0
    

    
    
    #for x in range(0, 20):
        #print(x) asi se hacen fors

print(sumando(100, 2))


"""
que recibas 2 numeros, 1 el numero que vas a sumar y 2 cuantas
 veces le vas a suamr 25
Es decir si das 3 y 8
3 + 200
Si das 450 y 1 que de 450 + 25 = 475
Obviamente tu solo regresas el numero final
Y ya mas dificil
encontre  este en una pagina Generar la secuencia de Fibonacci hasta un número n
Crear una función llamada fibonacci que reciba un número entero n como parámetro y devuelva una lista con la secuencia de Fibonacci hasta el número n.

python

def fibonacci(n):
    # Aquí irá el código
Inicializar una lista con los dos primeros números de la secuencia de Fibonacci: 0 y 1.

def fibonacci(n):
    secuencia = [0, 1]
    # Continuar el código

Utilizar un ciclo for para generar el resto de la secuencia hasta que la longitud de la lista sea igual a n.


def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        siguiente = secuencia[i-1] + secuencia[i-2]
        secuencia.append(siguiente)
    return secuencia
Mejorar la función para manejar casos donde n es menor o igual a 0, y cuando n es 1.
Crear otra función llamada imprimir_fibonacci que llame a la función fibonacci y luego imprima la secuencia de forma ordenada.
imprimir_fibonacci(7)  # Imprime: 0 1 1 2 3 5 8
si es necesario investiga que son los numeros fibonacci
"""
