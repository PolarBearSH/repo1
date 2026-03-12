from collections.abc import Iterable
class MyList:
    def __init__(self,*args,**kwargs):
        self.l=[]
        for i in args:
            self.l.append(i)
        for j in kwargs.values():
            self.l.append(j)
    def index_validation(self,i):
        if not isinstance(i,int):
            raise ValueError("Index has to be an integer")
        if i<0:
            if abs(i)>len(self.l):
                raise IndexError("Index out of range")
        else:
            if i>=len(self.l):
                raise IndexError("Index out of range")
        return True
    def __getitem__(self,num):
        self.index_validation(num)
        return self.l[num]
    def __setitem__(self,num,other):
        self.index_validation(num)
        print(f"{self.l[num]} Set successfully to {other}")
        self.l[num]=other
    def append(self,other):
        print(f"{other} successfully appended to {self.l} + {other}")
        self.l.append(other)
    def extend(self,x):
        if not isinstance(x,Iterable):
            raise TypeError("Has to be an iterable")
        print(f"{x} successfully extended to {self.l} + '{x}'")
        self.l.extend(x)
    def remove(self,x):
        if x in self.l:
            self.l.remove(x)
        else:
            print("Item not found in the list")
    def pop(self,i=''):
        if i=='':
            print("Successfully removed the last item")
            self.l.pop()
            
        else:
            if self.index_validation(i):
                print(f"Successfully removed the item at index {i}")
                self.l.pop(i)
    def insert(self,i,elem):
        self.index_validation(i) 
        self.l.insert(i,elem)
        print(f"'{elem}' successfully inserted at index {i}")
    def clear(self):
        self.l.clear()
        print("List cleared.")

    def index(self,val):
        for i,item in enumerate(self.l):
            if item==val:
                return i 
        return "Value not in list"
    def count(self,val):
        return self.l.count(val)
    def sort(self):
        if not self.l:
            return self.l
        t = type(self.l[0])
        for i in self.l:
            if type(i) not in (int,float):
                if not type(i)==t:
                    raise ValueError("< not supported between instances of this list")
        self.l.sort()
    def reverse(self):
        self.l=self.l[::-1]


    def copy(self):
        new_lst = self.l[:]
        return MyList(*new_lst)

    def __len__(self):
        return len(self.l)
    def __repr__(self):
        return f"{self.l}"

nums=MyList(6,7,a=1,b=2,c=4)
nums[1]=100
nums.append(90)
print(nums[1])
print(nums)
nums.extend("5")
nums[-1]=len(nums)
for i in nums:
    print(i)
# nums.insert(5,"hello")
print(1001 in nums)
nums.sort()
print(nums)
print(sum(nums))
a=nums.copy()
a[-1]=8000
print(a)
print(nums)
print(nums.reverse())
print(nums.count(6))
# 1․ Գրել MyList class, որը կունենա գրեթե բոլոր այն մեթոդները և ֆունկցիոնալությունը, որը ունի list class-ը առանց ժառանգելու։
#    Կլասի ներսում կարող եք պահել լիստ և օգտագործել լիստի մեթոդները։
#    Ավելացրեք մեթոդներ, որոնք կուզեիք, որ լիստերն ունենային, բայց չունեն։