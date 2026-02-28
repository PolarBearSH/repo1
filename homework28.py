# 1. Գրել Animal ծնող class՝ eat() և sleep() մեթոդներով: 
#    - Այս մեթոդներից յուրաքանչյուրը պետք է վերադարձնի համապատասխան հաղորդագրություն, երբ կանչ է արվում։
#    - eat()-ը պետք է վերադարձնի "Animal is eating..." հաղորդագրությունը
#    - sleep()-ը պետք է վերադարձնի "Animal is sleeping..." հաղորդագրությունը
#    Ծրագիրը պետք է ներառի նաև երկու ժառանգ class-ներ, որոնք ժառանգում են Animal class-ը՝ Bird և Fish: 
#    Այս class-ները Animal class-ից պետք է ժառանգեն sleep() մեթոդը, բայց նաև պետք է ներառեն իրենց մեթոդները՝ ներկայացնելու համար կենդանիներին բնորոշ վարքագիծը:
#    - Bird class-ում, փոփոխեք eat() մեթոդը՝ "Bird is pecking at its food..." հաղորդագրությունը վերադարձնելու համար։
#    - Բացի այդ, ներառեք fly() մեթոդը, որը վերադարձնում է "Bird is flying..." հաղորդագրությունը:
#    - Fish class-ում ներառեք swim() մեթոդը, որը վերադարձնում է "Fish is swimming..." հաղորդագրությունը:

class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")

class Bird(Animal):
    def eat(self):
        print("Bird is pecking at its food...")
    def fly(self):
        print("Bird is flying...")
class Fish(Animal):
    def swim(self):
        print("Fish is swimming...")

# a = Animal()
# b = Bird()
# f = Fish()
# a.sleep()
# b.fly()
# b.eat()
# f.swim()
# f.eat()
# f.sleep()
    



# 2․ Գրել Shape abstract class, որը․
#    - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
#    Գրել Circle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի շրջանագծի շառավիղը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։
#    Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։
#    Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի 
#      -- կամ եռանկյան երեք կողմերը,
#      -- կամ մեկ կողմը և բարձրությունը,
#      -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը, 
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
#    - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
#    - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
#      1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
#      2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
#      3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։


from abc import ABC,abstractmethod
from math import pi,sin,cos,radians
class Shape:
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        if radius<=0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    def perimeter(self):
        return 2*pi*self.radius
    def area(self):
        return pi*self.radius**2

class Rectangle(Shape):
    def __init__(self,length,width):
        if length<=0 or width<=0:
            raise ValueError("Lenght/Width has to be positive")
        self.length = length
        self.width = width
    def perimeter(self):
        return 2*self.length + 2*self.width 
    def area(self):
        return self.length*self.width

class Triangle(Shape):
    def __init__(self,*,a=None,b=None,c=None,h=None,alpha=None):
        if a is not None and b is not None and c is not None:
           if self.validate(a,b,c):
            self.a = a
            self.b = b
            self.c = c
            self.way = 1
    
        elif h is not None:
            if a is not None:
                if self.validate_way2(a,h):
                    self.a = a
                    self.h = h
            elif b is not None:
                if b<=0:
                    raise ValueError("Invalid side")
                self.b = b
                self.h = h
            elif c is not None:
                if c<=0:
                    raise ValueError("Invalid side")
                self.c = c
                self.h = h
            self.way = 2
        elif alpha is not None:
            if alpha<=0 or alpha>=180:
                raise ValueError("Invlaid angle")
            if a is not None:
                if a<=0:
                    raise ValueError("Invalid side")
                if b is not None:
                    if b<=0:
                        raise ValueError("Invalid side")
                    self.a = a
                    self.b =b 
                elif c is not None:
                    if c<=0:
                        raise ValueError("Invalid side")
                    self.a = a
                    self.c =c
            if b is not None:
                if b<=0:
                        raise ValueError("Invalid side")
                if c is not None:
                    if c<=0:
                        raise ValueError("Invalid side")
                    self.b=b 
                    self.c=c 
            self.alpha=alpha    
            self.way = 3
        else:
            raise ValueError("Not enough info to create triangle")

    def perimeter(self):
        if self.way==1:
            return self.a+self.b+self.c 
        elif self.way==2:
            return "Impossible to calculate with only height and base"
        elif self.way==3:
            c = (self.a**2+self.b**2 - 2*self.a*self.b*cos(radians(self.alpha)))**0.5
            return self.a + self.b + c 
    def area(self):
        if self.way==1:
            p = self.perimeter()/2 
            return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5        
        elif self.way==2:
            return self.a*self.h/2 
        elif self.way==3:
            return self.a * self.b * sin(radians(self.alpha))/2
    @staticmethod
    def validate(a,b,c):
        if a>=b+c or b>=a+c or c>=a+b:
            raise ValueError(f"Non-existing triangle with sides {a},{b},{c}")
        if a<=0 or b<=0 or c<=0:
            raise ValueError("Sides must be positive")
        return True
    @staticmethod
    def validate_way2(side,h):
        if side<=0:
            raise ValueError("Invalid Side")
        elif h<=0:
            raise ValueError("Invalid Height")
        return True
t1 = Triangle(a=3,b=4,c=5)
t2 = Triangle(a=4,h=10)
t3 = Triangle(a=3,b=13,alpha=90)
ls = [t1,t2,t3]
for i in ls:
    print(i.perimeter())
    print(i.area())
    print("=========================")
