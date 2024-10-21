#Programa  que genera numeros primos mediante funciones de manera infinita 
def isPrime(number):
    if number%5==0:#%es la operacion modulo
        return False
    else:
        return True
    

def generatePrime(limit):
    primes = []
    for num in range(0,limit+1):
        if isPrime(num):
            primes.append(num)#.append para meter alementos al final de una lista 

    return primes

userLimit=int(input("Introduce el imite hasta donde quieres contar: "))

listOfNumbers= generatePrime(userLimit)
print(listOfNumbers)