# Cajero automatico
while True:
    saldo=1000
    nuevoSaldo=0

    print("*****Bienvenido al Cajero Automatico***")
    print("        ***Menu***          ")
    print("a. Cosultar saldo")
    print("b. Depositar dinero")
    print("c. Retirar dinero")
    print("d. salir ")
    opcion=input("ingrese la opcion que desea: a, b, c o d: ")

    if opcion != "a" and opcion !="A" and opcion != "b" and opcion !="B" and opcion != "c" and opcion !="C" and opcion != "d" and opcion !="D":
        print("opcion invalida(a.b.c o d)")

    elif opcion =="a" or opcion=="A":
            print("su saldo es:", saldo)

    elif opcion=="b" or opcion =="B":
       # def deposito(n):
            n=float(input("Ingrese la Cantidad que desea depositar"))
            while n <=0:
                print("cantidad Erronea intenta nuevamente")
            if n >0:
                nuevoSaldo=saldo+n
        
                print("su nuevo saldo es:", nuevoSaldo)
            #return n
    elif opcion=="c" or opcion=="C":
                #def retiri(j):    
                    j=float(input("Ingrese la cantidad que desea retirar:"))
                    if j <=0:
                        print("cantidad Erronea intenta nuevamente")
                    elif j >0:
                            nuevoSaldo=saldo-j
                            print("su nuevo saldo es:", nuevoSaldo)
                            if nuevoSaldo<saldo:
                                print("no puede retirar esta cantidad(saldo insuficiente):")
                   # return j 


    elif opcion =="d" or opcion=="D":
        print("**Gracias por usar nuestro cajero:")
        print()
else:
    False












