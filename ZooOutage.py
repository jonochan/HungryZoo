from AnimalClasses import Antelope
from AnimalClasses import BigFish
from AnimalClasses import Bug
from AnimalClasses import Bear
from AnimalClasses import Chicken
from AnimalClasses import Cow
from AnimalClasses import Fox
from AnimalClasses import Giraffe
from AnimalClasses import Lion
from AnimalClasses import Panda
from AnimalClasses import Sheep
from AnimalClasses import LittleFish
from AnimalClasses import Grass
from AnimalClasses import Leaves



animalList = {
    "antelope": 1,
    "big-fish": 2,
    "bug": 3,
    "bear": 4,
    "chicken": 5,
    "cow": 6,
    "fox": 7,
    "giraffe": 8,
    "lion": 9,
    "panda": 10,
    "sheep": 11,
    "grass": 12,
    "leaves": 13,
    "littlefish": 14
    }

def createObj(x):
    if x ==1:
        obj = Antelope()
        return obj
    elif x==2:
        obj = BigFish()
        return obj
    elif x==3:
        obj = Bug()
        return obj
    elif x==4:
        obj = Bear()
        return obj
    elif x==5:
        obj = Chicken()
        return obj
    elif x==6:
        obj = Cow()
        return obj
    elif x==7:
        obj = Fox()
        return obj
    elif x==8:
        obj = Giraffe()
        return obj
    elif x==9:
        obj = Lion()
        return obj
    elif x==10:
        obj = Panda()
        return obj
    elif x==11:
        obj = Sheep()
        return obj
    elif x==12:
        obj = Grass()
        return obj
    elif x==13:
        obj = Leaves()
        return obj
    else:
        obj = LittleFish()
        return obj
    return "error"



    

def eat(menu):
    currentItem = ""
    remaining = []
    for x in range(len(menu)):
        currentChar = menu[x].lower()
        if currentChar == ",":
            animalNum = animalList.get(currentItem)
            animal = createObj(animalNum)
            remaining.append(animal)
            currentItem = ""
        else:
            currentItem = currentItem + currentChar
    animalNum = animalList.get(currentItem)
    animal = createObj(animalNum)
    remaining.append(animal)
    feasting = True
    count = 0
    isLeft = True
    ret=[]
    text = ""
    while feasting:
        result = check(remaining, count)
        if result == "left":
            text =  remaining[count].type() + " eats "+ remaining[count-1].type()
            ret.append(text)
            del remaining[count-1]
            count = 0
        elif result == "right":
            text =  remaining[count].type() + " eats "+ remaining[count+1].type()
            ret.append(text)
            del remaining[count+1]
            count = 0
        elif result == "both":
            text =  remaining[count].type() + " eats "+ remaining[count-1].type()
            ret.append(text)
            text =  remaining[count].type() + " eats "+ remaining[count+1].type()
            ret.append(text)
            del remaining[count+1]
            del remaining[count-1]
            count = 0
        else:
            count = count +1
            if count > len(remaining)-1:
                feasting = False


    
    for x in range(len(remaining)):
        ret.append(remaining[x].type())
    return ret
            
                    
                    


def check(remainingAnimals, count):
    currentAnimal = remainingAnimals[count]
    length = len(remainingAnimals)
    foodList = currentAnimal.eat()
    listSize = len(foodList)
    tally = 0
    if length ==1:
        return ""
    if count == 0:
        right = remainingAnimals[1].type().lower()
        for x in range(listSize):
            if foodList[x] == right:
                tally = tally + 2
    else:
        left = remainingAnimals[count-1].type()
        for y in range(listSize):
            if foodList[y] == left.lower():
                tally = tally + 1
        if count+1 < length:
            right = remainingAnimals[count+1].type()
            for x in range(listSize):
                if foodList[x] == right.lower():
                    tally = tally + 2
    if tally ==2:
        return "right"
    elif tally == 1:
        return "left"
    elif tally == 3:
        return "both"
    else:
        return ""
    return ""





#menu = "fox,bug,chicken,grass,sheep"
menu = "fox,bug,grass,leaves,chicken,bear,lion,antelope,sheep,grass,panda,leaves,lion"
result = eat(menu)
finalResult = []
finalResult.append(menu)
length = len(result)
for x in range(length):
    finalResult.append(result[x])
print(finalResult)

















