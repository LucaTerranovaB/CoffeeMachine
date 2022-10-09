from principal import CoffeeMachine
from principal import Items



r = 'y'
while r == 'y': 
    
        
        print("Bienvenido!!")
        print("****************************\n")
        print("INGRESE LAS MONEDAS")
        print("-------------------------------------------")
        print("Precios:\n") 
        print("--> Cafe sin azucar = 1 moneda\n--> Cafe con azucar = 2 monedas\n--> Cafe con leche sin azucar = 3 monedas\n--> Cafe con leche con azucar = 4 monedas")

       
        coins = int(input(print("-------------------\nINGRESE LA CANTIDAD DE MONEDAS : \t")))
        h = CoffeeMachine(2000,2000,150,100,20,coins)
       
       
        print("1-> Cafe sin azucar\n2-> Cafe con azucar\n3-> Cafe con leche sin azucar\n4-> Cafe con leche con azucar")
        print("---------------------------------------------")
        eleccion = int(input(print("INGRESA LA BEBIDA QUE DESEA : \n")))
    
        
        if eleccion < 4:

            if eleccion == 1 and coins >=1:
                a = CoffeeMachine(150,0,10,0,0,1).cafeSinAzucar(150,10,1)
                print(a)
                print("\n-------------------------------------------")
        
            elif eleccion == 1 and coins < 1:
                print("EL valor supera a las monedas que ingreso")
            elif eleccion == 2 and coins >= 2:
                b = CoffeeMachine(150,0,10,6,0,2).cafeConLecheSinAzucar(150,100,10,2)
                print(b)
                print("\n-------------------------------------------")
            elif eleccion == 2 and coins < 2:
                print("EL valor supera a las monedas que ingreso")
            elif eleccion == 3 and coins >= 3:
                c = CoffeeMachine(50,100,10,0,0,3).cafeConLecheSinAzucar(50,100,10,3)
                print(c)
                print("\n-------------------------------------------")
            elif eleccion == 3 and coins < 3:
                print("EL valor supera a las monedas que ingreso")
            elif eleccion == 4 and coins >= 4:
                d = CoffeeMachine(50,100,10,6,0,4).cafeConLecheConAzucar(50,100,10,6,4)
                print(d)
                print("\n-------------------------------------------")
            elif eleccion ==4 and coins < 4:
                print("EL valor supera a las monedas que ingreso")     
        
        else:
            print("Ha ingresado una opcion invalida")
        r = input(print("Ingrese: 's' para SI, 'n' para NO"))

if __name__=='__main__':
    a = CoffeeMachine()
    print(a.cafeSinAzucar())
    b = CoffeeMachine()
    print(b.cafeConAzucar())
    c = CoffeeMachine()
    print(c.cafeConLecheSinAzucar())
    d = CoffeeMachine()
    print(d.cafeConLecheConAzucar())
    



