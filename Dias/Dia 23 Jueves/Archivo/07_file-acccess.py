#como usar documentos externos

lista=[]
archivo= open("devices.txt")
for item in archivo:
    item= item.strip()
    lista.append(item)
    print(item)
archivo.close()
