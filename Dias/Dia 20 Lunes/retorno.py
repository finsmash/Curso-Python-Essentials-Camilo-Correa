#formas de pasar a argumentos 
#puede usar retorno de valor en funciones
#esto ayuda a que la funcion devuelva algun valor
def multi(num1,num2):
    print("El resultado de multiplicar",num1,"*",num2,
          "es: ",num1*num2)
    return (num1*num2)
multi(50, num2=6)
multi(num1=50, num2=6)
multi(50,87)
resultado=multi(50,87)

opt=resultado+1.12

print(opt)
