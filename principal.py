# 1 Hacemos un analisis de las clases 

from ast import Raise
from msilib.schema import Error
from pkg_resources import safe_extra


class Items:

    def __init__(self,agua,leche,cafe,azucar,vainilla,coins=int):

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



    def cafeConAzucar(self,agua,cafe,azucar,coins):

        agua -= 150
        cafe -= 10
        azucar -= 6
        coins -= 2

       
    
    def cafeConLecheSinAzucar(self,agua,leche,cafe,coins):

        agua -= 50
        cafe -= 10
        leche -= 100
        coins -= 3
        
   

    def cafeConLecheConAzucar(self,agua,leche,cafe,azucar,coins):

        agua -= 50
        cafe -= 10
        leche -= 100
        azucar -= 6
        coins -= 4
       



    
if __name__=='__main__':
    a = CoffeeMachine.cafeSinAzucar
    b = CoffeeMachine.cafeConAzucar
    c = CoffeeMachine.cafeConLecheSinAzucar
    d = CoffeeMachine.cafeConLecheConAzucar
    
    
    
