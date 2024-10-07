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