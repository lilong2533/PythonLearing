#-*- coding: UTF-8 -*-

class Fruit:
    price = 0
    
    def __init__(self ,color ,zone):
        self.__color = color
        self.zone = zone
        Fruit.price += 1
        print color ,' : ' ,zone
        
    def __doc__(self):
        return self.__color ,self.zone
    
class FruitShop(object):
    __instance = None
    
    def __new__(cls ,*args ,**kwd):
        if FruitShop.__instance == None:
            FruitShop.__instance = object.__new__(cls, *args ,**kwd)
            FruitShop.__instance.list = []
            FruitShop.__instance.name = args[0]
            print '__new__  : ' ,FruitShop.__instance 
        return FruitShop.__instance
        
    def __init__(self ,*args ,**kwd):
        print '__init__  : ' ,self
        pass
        
    def addFruit(self, fruit):
        self.list.append(fruit);