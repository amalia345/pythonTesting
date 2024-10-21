#Tablas de multiplicar del 1-10 para un numero que da el usuario.
def tablaMultiplicar(numero, limite):
    for multiplo in range(1,limite+1):
        print(f" {numero} x {multiplo} = {numero*multiplo}")#string


print("\nEste prgrama es para mostrar las tablas de multiplicación\n El primer nñumeri es la tabla que quieres y el segundahasta donde quieres que llegue")
numeroUsuario=int(input("Introduce el numero: "))
usuarioLimite=int(input("Cuantas veces quieres multiplicar este numero?"))
tablaMultiplicar(numeroUsuario, usuarioLimite)

    
#input 





