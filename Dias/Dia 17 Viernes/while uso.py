#uso del mientras (while)

num_contar=input("Ingrese el # al que debo contar:")
num_contar=int(num_contar)
contador=1

"""
while (contador<=num_contar):
    print(contador)
    contador+=1
    if contador>num_contar:
        break
"""
print("antes del while")
while (True):
    print(contador)
    contador+=1
    if contador>num_contar:
        break
    print("dentro del bucle")
print("Fin del programa")
    