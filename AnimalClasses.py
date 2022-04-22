from abc import ABC, abstractmethod



class Plant(ABC):
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Plant"
        self.name = name
        self.age = age
        self.alive = alive
        self.weight = weight
        
    #Methods
    @abstractmethod
    def eat(self):
        pass

class Leaves(Plant):
    #Attributes
    

    #Constructors
    def __init__(self):
        self.value = "Leaves"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return []
    def move(self):
        return ""

class Grass(Plant):
    #Attributes
    

    #Constructors
    def __init__(self):
        self.value = "Grass"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return []
    def move(self):
        return ""

class Animal(ABC):

    #Attributes
    age = None
    alive = True
    name = "Nameless"
    
    #Constructors
    def __init__(self):
        self.value = "Animal"
    
        

    #Methods
   

    @abstractmethod
    def eat(self):
        pass

    def type(self):
        return self.value

    
class Insect(Animal):
    
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Insect"
    #Methods
    @abstractmethod
    def eat(self):
        pass
    

    def type(self):
        print(self.value)
        

class Bug(Insect):
    #Attributes
    

    #Constructors
    def __init__(self):
        self.value = "bug"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["leaves"]
    def move(self):
        return "I crawl"
        
class Fish(Animal):
    
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Fish"
    #Methods
    @abstractmethod
    def eat(self):
        pass

    def type(self):
        print(self.value)

class BigFish(Fish):
    #Attributes
    

    #Constructors
    def __init__(self):
        self.value = "big-fish"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["little-fish"]

class LittleFish(Fish):
    #Attributes
    

    #Constructors
    def __init__(self):
        self.value = "big-fish"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return []

class Bird(Animal):
    
    #Attributes
    
    #Constructors
    def __init__(self):
        super().__init__(name)
        self.value = "Bird"
    #Methods
    @abstractmethod
    def eat(self):
        pass
    

    def type(self):
        print(self.value)
        

class Chicken(Bird):
    #Attributes
    

    #Constructors
    def __init__(self):
        self.value = "Chicken"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["bug"]


    
class Mammal(Animal):
    #Attributes
    numLegs = 4

    #Constructors
    def __init__(self):
        self.value = "Mammal"


    #Methods
    @abstractmethod
    def eat(self):
        pass
    

    def type(self):
       return self.value


class Antelope(Mammal):
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Antelope"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["grass"]
  

class Bear(Mammal):
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Bear"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["big-fish", "bug","chicken","cow","leaves", "sheep"]
 


class Fox(Mammal):
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Fox"
        
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["sheep", "chicken"]

class Lion(Mammal):
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Lion"
        
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["antelope","cow"]
    
class Panda(Mammal):
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Panda"
        
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["leaves"]

class Giraffe(Mammal):
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Giraffe"
        
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["leaves"]
    
class Sheep(Mammal):
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Sheep"
        
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["grass"]


class Cow(Mammal):
    #Attributes
    
    #Constructors
    def __init__(self):
        self.value = "Cow"
        
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return ["grass"]

