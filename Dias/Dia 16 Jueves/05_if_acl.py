#if y else, and elif 

acl= int(input("Ingrese el # de ACL"))
if acl >=1 and acl <=99:
    print("La ACL es estandar")
elif acl >=100 and acl <=199:
    print("La ACL es extendida")
else:
    print("El dato ingresado no es un ACL")
