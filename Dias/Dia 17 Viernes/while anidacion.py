#ejemplo while como anidar bien 

while True:
    x=input("Ingresa un numero hasta el que contar:")
    if x=="q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
        
        

