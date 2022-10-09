# 1 Hacemos un analisis de las clases 

from pkg_resources import safe_extra


class Items:

    def __init__(self,agua,leche,cafe,azucar,vainilla,coins):

        self.agua = 2000
        self.leche = 2000
        self.cafe = 150
        self.azucar = 100
        self.vainilla = 35
        self.coins = coins


    def refill(self):

        if self.agua < 150:
            print("Please refill Water")
        else:
            if self.leche < 70:
                print("Please refill milk")
            else: 
                if self.azucar < 6:
                    print("Please refill sugar")
        
        
        a = input("Do you want to refill? (y/n)")
        x = input(print("Ingrese la cantidad de agua agregada"))
        b =input(self.agua + x) 
        y = input(print("Ingrese la cantidad de leche agregada"))
        c = (self.leche + y)
        z = input(print("Ingrese la cantidad de azucar agregada"))
        d = (self.azucar + z)   

class CoffeeMachine :

    def __init__(self,agua,leche,cafe,azucar,vainilla,coins):

        self.agua = agua
        self.leche = leche
        self.cafe = cafe
        self.azucar = azucar
        self.vainilla = vainilla
        self.coins = 0

    def insert_coin(self,coins):
        
        self.coins += 1
         

    def cafeSinAzucar(self,agua,cafe,coins):
        
        agua -= 150
        cafe -= 10
        coins -= 1
        print("///////////////////////////////////////////////////")
        print("\t SU BEBIDA ESTA LISTA")

    def cafeConAzucar(self,agua,cafe,azucar,coins):

        agua -= 150
        cafe -= 10
        azucar -= 6
        coins -= 2
        print("///////////////////////////////////////////////////")
        print("\t SU BEBIDA ESTA LISTA")

    def cafeConLecheSinAzucar(self,agua,leche,cafe,coins):

        agua -= 50
        cafe -= 10
        leche -= 100
        coins -= 3
        print("///////////////////////////////////////////////////")
        print("\t SU BEBIDA ESTA LISTA ")

    def cafeConLecheConAzucar(self,agua,leche,cafe,azucar,coins):

        agua -= 50
        cafe -= 10
        leche -= 100
        azucar -= 6
        coins -= 4
        print("///////////////////////////////////////////////////")
        print("\t SU BEBIDA ESTA LISTA")


r = input(print("Quiere otro cafe?\n-->'y' Para SI\n-->'n' para NO"))


if __name__=='__main__':
    a = CoffeeMachine(150,0,10,6,0,1).cafeSinAzucar(150,10,1)
    print(a)
    b = CoffeeMachine(150,0,10,6,0,2).cafeConAzucar(150,10,6,2)
    print(b)
    c = CoffeeMachine(50,100,10,0,0,3).cafeConLecheSinAzucar(50,100,10,3)
    print(c)
    d = CoffeeMachine(50,100,10,6,0,4).cafeConLecheConAzucar(50,100,10,6,4)
    print(d)
    
   