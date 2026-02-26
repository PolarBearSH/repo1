import string,time,smtplib,random,os
class AgeError(Exception):
        pass
class MoneyError(Exception):
    pass
class PinError(Exception):
    pass
class CardError(Exception):
    pass


class BankUser:
    count=0
    access=True
    @staticmethod
    def validate(v):
        if not v:
            raise ValueError("Enter NAME/SURNAME (A-Z).")
        return v.isalpha() and all(ch in string.ascii_letters for ch in v)

    @staticmethod  
    def validate_age(a):
        if not isinstance(a,int) or a>115:
            raise AgeError("Invalid age")
        elif a<18:
            raise AgeError("Age CANNOT be below 18")
        return True

    
    @staticmethod  
    def validate_gmail(gm):
        if not gm:
            raise ValueError("Enter gmail Address")
        elif len(gm)<=10:
            raise ValueError("Invalid gmail Address")
        len_gmail = 10 
        s,i='',-1

        while len_gmail>0:
            s+=gm[i]
            i-=1
            len_gmail-=1 
        return s[::-1]=="@gmail.com" and gm[:i].isalnum()

    @staticmethod  
    def validate_card_number(num):
        def luhn(n):
            n=str(n)
            summa=0
            for i in range(0,16,2):
                m=str(int(n[i])*2)
                if len(m)==2:
                    summa+=int(m[0])+int(m[1])
                else:
                    summa+=int(m)
            for i in range(1,16,2):
                summa+=int(n[i])
            if summa%10==0:
                return True 
            return False
        if len(str(num))==16:
            return luhn(num)
        else:
            raise CardError("Card Number must have 16 digits")
    @staticmethod   
    def validate_pin(p):
        return len(str(p))==4
    @staticmethod
    def validate_money(m):
        if m<=0:
            raise MoneyError("Enter positive integer") 
        

#--------------------------------------------------------------------------------------
            
    def __init__(self, name, surname, age, gmail, card_number, money, pin):

        if not (self.validate(name) and self.validate(surname)):
            raise ValueError("NAME/SURNAME have to be in latin letters (A-Z).")
        
        self._name=name
        self._surname=surname 

        if self.validate_age(age):
            self.age=age

        if not self.validate_gmail(gmail):
            raise ValueError("Invalid email")
        self._gmail=gmail
        
            
        if not self.validate_card_number(card_number):
            raise CardError("Non-existing card number")
        self.__card_number = card_number 

        self.validate_money(money)
        self.__money=money
        
        if not self.validate_pin(pin):
            raise PinError("__pin has to be 4 digits")
        self.__pin=pin
        
            
            


    def person(self):
        if BankUser.access:
            return f"CARDHOLDER: {self._name.upper()} {self._surname.upper()}"
        
        return "No Acess to Cardholder data" 
    def card_data(self):
        if BankUser.access:
            user = int(input("Enter the pin code: "))
            if user == self.__pin:
                self.pend()
                return f"CARD NUMBER: {self.__card_number}, ${self.__money:02d}"
        else:
            return "No Access to Card Data"
    def deposit(self):
        if BankUser.access:
            user = int(input("Enter the pin code: "))
        
            if user==self.__pin:
                d = int(input("Enter Amount to Deposit: "))
                self.validate_money(d)
                self.__money+=d
                self.pend()
                return "Successful!"
            else:
                
                print("Incorrect pin code!\n")
                BankUser.count+=1
                
                if BankUser.count==3:
                    BankUser.access=False
                    return "Account Blocked!"

                return self.withdraw()
        
        return "No Access to Deposit"

    def withdraw(self):
        if BankUser.access:
            user = int(input("Enter the pin code: "))
            
            if user==self.__pin:
                d = int(input("Enter Amount to Withdraw: "))
                self.validate_money(d)
                
                if self.__money-d<0:
                    self.pend()
                    return "Not enough funds."
                self.pend()
                self.__money-=d
                return "Successful!"
            else:
                
                print("Incorrect pin code!\n")
                BankUser.count+=1
                
                if BankUser.count==3:
                    BankUser.access=False
                    return "Account Blocked!"
                return self.withdraw()
        
        return "No Access to Withdrawing"
    
    def restore(self):
        if not BankUser.access:
            print("Enter the 6-digit number sent to your email")
            sender_email = "hovhannisianshushank@gmail.com"
            receiver_email = input("Enter your email: ")
            self.validate_gmail(receiver_email)
            random_num = random.randint(100000,999999)
            context = f"Subject: Important! \n\n Your recovery digits {random_num}"
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(sender_email,os.getenv("EMAIL_PASSWORD"))
            server.sendmail(sender_email,receiver_email,context)
            print("Email has been sent.")
            server.quit()
            digits = int(input("Digits: "))
            if digits==random_num:
                BankUser.access=True
                return "Done"
            else: 
                print("Incorrect. Resending an email\n")
                return self.restore()     
        return ""

    @staticmethod
    def pend():
        n=4
        while n>0:
            for dots in range(4):
                print("\rPending" + "."*dots,end="",flush=True)
                time.sleep(0.5)
            n-=2
        print("\n")


user = BankUser("Peter","Collins",45,"hovhannisianshushank@gmail.com",4539148803436467,50,1111)

print(user.person())
print(user.withdraw())
print(user.card_data())
print(user.restore())
print(user.deposit())
print(user.card_data())









