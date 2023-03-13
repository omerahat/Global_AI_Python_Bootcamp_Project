import csv
import datetime 


class Pizza():
    def __init__(self,pizza_description,pizza_cost):
        self.description = pizza_description
        self.cost = pizza_cost

    def get_description(self):
        return self.description
    def get_cost(self):
        return self.cost
    
class Classic(Pizza):
    description= "Classic"
    cost= 20
    def __init__(self,description, cost):
        Pizza.__init__(self, description,cost)
            
class Margherita(Pizza):
    description = "Margherita"
    cost= 25
    def __init__(self, description, cost):   
            Pizza.__init__(self, description, cost)
            Pizza.get_cost(cost)
            Pizza.get_description(description)
              
class Turkish_Pizza(Pizza):
    description = "Turkish"
    cost= 30
    def __init__(self, description, cost):
            
            print(self.description)
            Pizza.__init__(self, description, cost)
            
class Dominos_Pizza(Pizza):
    description = "Dominos"
    cost= 20
    def __init__(self, description, cost):
            Pizza.__init__(self, description, cost)
        
class Decorator(Pizza):
    
    def __init__(self, component):
        Pizza.__init__(self,component)
        self.cost=0
        self.description = " "
        self.component = component

    def get_cost(self):
       return self.cost
    def get_description(self):
       return self.description

class Olive(Decorator):
    description = "Olive"
    cost = 6
    def __init__(self,description,cost):
        Decorator.__init__(self,description,cost)
        
class Mushroom(Decorator):
    description = "Mushroom"
    cost = 8
    def __init__(self, description,cost):
        Decorator.__init__(self,description,cost)
    

class GoatCheese(Decorator):
    description = "Goat Cheese"
    cost = 8
    def __init__(self, description,cost):
        Decorator.__init__(self,description,cost)


class Meat(Decorator):
    description = "Meat"
    cost = 10
    def __init__(self, description,cost):
        Decorator.__init__(self,description,cost)

class Onion(Decorator):
    description = "Onion"
    cost = 4
    def __init__(self, description,cost):
        Decorator.__init__(self,description,cost)

class Corn(Decorator):
    description = "Corn"
    cost = 5
    def __init__(self, description,cost):
        Decorator.__init__(self,description,cost)  