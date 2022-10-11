
import unittest


from principal import *

from principal import CoffeeMachine 


#Crear tantos test como metodos tenga el programa
#Posibilidad de 2 test por metodo para escenario feliz t triste
class CoffeMachineTest(unittest.TestCase):
    
    def test_initial(self):
        machine = CoffeeMachine(2000,2000,150,100,20,0)
        self.assertEqual(machine.coins, 0)

    def test_insert_coin(self):
        machine = CoffeeMachine(2000,2000,150,100,20,0)
        machine.insert_coin(1)
        self.assertEqual(machine.coins, 1)

    def test_cafe_sin_azucar(self):

        coffee = CoffeeMachine(2000,2000,150,100,20,1)
        coffee.cafeSinAzucar(150,10,1)
        self.assertEqual(coffee.agua >= 150,coffee.cafe >= 10, coffee.coins >=1)

    def test_sin_ingredientes(self):

        pedido = CoffeeMachine(50,50,5,5,5,1).cafeSinAzucar(150,10,1)
        self.assertEqual(pedido, None)

    def test_sin_pagar(self):

        pedido = CoffeeMachine(2000,2000,150,100,20,1).cafeConLecheConAzucar(50,10,100,6,4)
        self.assertEqual(pedido, None)


    
    def test_refill_ok(self):

        peticion = Items(0,0,0,0,0,0).refill()
        self.assertFalse(peticion,None)



    def test_refill_wrong(self):

        peticion = Items(2000,2000,150,100,20,0).refill()
        self.assertFalse(peticion)



if __name__ == '__main__':
    unittest.main()

