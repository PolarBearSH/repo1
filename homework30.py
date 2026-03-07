# 1․ Գրել Calculator class, որը․
#    - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
#    - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
#    - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
#    - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__)։

class Calculator:
    def __init__(self,__num):
        if isinstance(__num,(int,float)):
            self.__num=__num
        else:
            raise ValueError("The number has to be integer or float")
    
    @property
    def get_num(self):
        return self.__num 
    
    def  __add__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return Calculator(self.__num+other)

    def __radd__(self,other):
        return self+other
    def __iadd__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        self.__num+=other 
        return self
    def  __sub__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return Calculator(self.__num-other)

    def __rsub__(self,other):
        return Calculator(other-self.__num)
    def __isub__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        self.__num-=other 
        return self

    def __mul__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return Calculator(self.__num*other)

    def __rmul__(self,other):
        return Calculator(other*self.__num)
    def __imul__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        self.__num*=other 
        return self 
    
    def __truediv__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return Calculator(self.__num/other)

    def __rtruediv__(self,other):
        return Calculator(other/self.__num)
    def __itruediv__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        self.__num/=other 
        return self 
    def __floordiv__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return Calculator(self.__num//other)
    def __rfloordiv__(self,other):
        return Calculator(other//self.__num)
    def __ifloordiv__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        self.__num//=other
        return self
    def __mod__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return Calculator(self.__num%other)
    def __rmod__(self,other):
        return Calculator(other%self.__num)
    def __imod__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        self.__num%=other
        return self
    def __pow__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return Calculator(self.__num**other)
    def __rpow__(self,other):
        return Calculator(other**self.__num)
    def __ipow__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        self.__num**=other
        return self
    def __gt__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return self.__num>other 
    def __lt__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return self.__num<other 
    def __eq__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return self.__num==other 
    def __ge__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return self.__num>=other 
    def __le__(self,other):
        if isinstance(other,Calculator):
            other=other.__num
        return self.__num<=other 
    def __str__(self):
        return f"Calculator({self.__num})"
    def __repr__(self):
        return f"Calculator({self.__num}), Type: {type(self.__num)}"
n = Calculator(5)
m = Calculator(4)
print(n)
print(repr(n/m))
# print(n-m)
# print(n+m)
# print(n*m)
# print(n/m)
# print(n//m)
# print(n%m)
# print(n**m)
# print(100+m)
# print(100-m)
# print(m-100)
# print(5*n)
# print(100/n)
# print(100**n+m)
# print(n>m)
# print(n<m)
# print(n>=m)
# print(n<=m)
# print(n==5)
# print(5==m)
# print(5>n)
# print(10000000<=n)
# print(n<=1000000000)