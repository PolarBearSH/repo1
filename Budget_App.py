#Built bundget app 
import math
class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount, 'description': description})
    def withdraw(self,amount,description=''):
        if self.get_balance()>=amount:
            self.ledger.append({'amount': -amount,'description': description})
            return True
        return False

    def get_balance(self):
        return sum(i['amount'] for i in self.ledger)

    def transfer(self,amount,ins:Category):
        if self.withdraw(amount,f"Transfer to {ins.name}"):
            ins.deposit(amount,f"Transfer from {self.name}")
            return True
        return False
        
    def check_funds(self,amount):
        if amount>self.get_balance():
            return False
        return True
    def __str__(self):
        #len(self.name)+2x = 30
        s=f"\033[32m{(30-len(self.name))//2*"*"+self.name+(30-len(self.name))//2*"*"}\033[0m"  #e.g. *************Food*************,
                                                                            # No matter how many chars the self.name is, i want the total length to be 30
        
        for i in self.ledger:
            s+=f"\n{i['description'][:23]:23}{i['amount']:7.2f}"
        s+=f"\nTotal: {self.get_balance():.2f}"                              
        return s
def create_spend_chart(categories):
    s=''
    s+="\033[31mPercentage spent by category \033[0m \n"
    tot1=0
    d={}
    for category in categories:
        for i in category.ledger:
            if i['amount']<0:
                tot1+= i['amount'] #calculating the total money withdrawed in every category
                if category in d:
                    d[category.name]+=abs(i['amount']) #creating a dictionary, where the values are total money withdrawed for each category separately
                else:
                    d[category.name]=abs(i['amount'])

    for k,v in list(d.items()): # suppose we have spent $100 in every category (bought food,clothes,paid the bills etc.), and 50,25,25 dollars separately in cat1,cat2,cat3 , so we spent the 50%,25%,25% of the total money,that's what the chart's gonna represent on decimal scale
        d[k] = math.floor(v*100/abs(tot1))
        d[k]-=d[k]%10
   
    for j in range(100,-1,-10):
        s += f"{j:3}| "
        for v in d.values():
            if v>=j:
                s+="o  "
            else:
                s+="   "
        s+="\n" 


    s+="    " + "-" * (len(d) * 3 + 1)+"\n"
   
    for i in range(len(max(d.keys(),key=len))):    
        s += "     "
        for k in d:
            if i<len(k):
                s+=k[i]+"  "
            else:
                s+="   "
        if i < len(max(d.keys(), key=len)) - 1:
            s+="\n"
        
    return s

cat1 = Category("Food")
cat2 = Category("Clothes")
cat3 = Category("Bills")
cat4 = Category("Pet")
cat5 = Category("Shopping")

cat1.deposit(900, 'deposit')
cat1.withdraw(45.67, 'restaurant and more food for dessert')

cat2.deposit(1500,'deposit')
cat2.withdraw(500, 'Nike Outwear')

cat3.deposit(200.5, 'deposit')
cat3.withdraw(150,"Water bill")

print(cat3)
print(create_spend_chart([cat1,cat2,cat3]))
