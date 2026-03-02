# 1․ Գրել MyShows class, որը․
#    - __init__ ում կստանա 
#      -- սերիալի անունը (պետք է լինի տեքստ),
#      -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ), 
#      -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
#      -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
#      -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
#      -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
#    - բոլոր ատրիբուտները կլինեն private,
#    - կունենա getter բոլոր ատրիբուտների համար,
#    - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
#    - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
#    - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
#    - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։
class RatingError(Exception):
    pass
class MyShows:
    def __init__(self,name:str,platform:str,year:int,cast:list,seria:int=1,rate:int=None):
        self.__name = name
        self.__platform = platform
        self.__year = year 
        self.__cast = cast 
        self.__seria = seria 
        self.rate_check(rate)
        self.__rate = rate
    @staticmethod
    def rate_check(r):
        if r<=0 or r>10:
            raise RatingError("Film must be rated on a scale 1-10")
    @property
    def name(self):
        return self.__name.title()
    @property
    def platform(self):
        return self.__platform.title()
    @property
    def year(self):
        return self.__year
    @property
    def cast(self):
        ans=''
        a=len(self.__cast)
        for i in range(a):
            if i==a-1:
                ans+=self.__cast[i].title()
            else:
                ans+=self.__cast[i].title()+", "
        return ans
    @property
    def seria(self):
        return self.__seria
   
    @property
    def rate(self):
        if self.__rate is None:
            return "-Not rated by the user-"
        return self.__rate
    
    @seria.setter
    def seria(self,val):
        self.__seria=val
    @rate.setter
    def rate(self,val):
        self.rate_check(val)
        self.__rate=val 
    @rate.deleter
    def rate(self):
        self.__rate=None
    def refresh_cast(self):
        print("Add or remove? (+/-):\n")
        while True:
            n=input()
            if n not in ("+","-"):
                print("Enter '+' to add, '-' to remove:\n")
            elif n=='-':
                name = input("Enter actor's name: ").title()
                if name in self.__cast:
                    self.__cast.remove(name)
                    print(f"Removed {name} from the cast")
                    break
                else:
                    print("Not found in the cast")
                    break
            else:
                name = input("Enter actor's name: ").title()
                if name not in self.__cast:
                    self.__cast.append(name)
                    print(f"Added {name} to the cast")
                    break
                else:
                    print("Already in the cast")
                    break
        
    def __str__(self):
        return f"------{self.__name}({self.__year})------\nRating: {self.rate}{"" if not self.rate else "\10"}\nCast: {self.__cast}\nEpisode: {self.__seria}\n{self.__platform}"

m=MyShows("breaking bad","kinopoisk",2008,["brian cranston","rian"],48,10)
print(m.seria)
print(m.rate)
print(m.name)
print(m.cast)
print(m.platform)
print(m.year)
m.rate = 5
m.seria = 30
print(m.seria)
print(m.rate)
del m.rate 
# m.rate=9
print(m.rate)
print(m)

