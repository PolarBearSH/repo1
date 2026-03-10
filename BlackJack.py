import random
import time
class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
        self.suits_dict = {"Spades":"\033[30m\u2660\033[0m","Hearts":"\033[31m\u2665\033[0m","Diamonds":"\033[31m\u2666\033[0m","Clubs":"\033[30m\u2663\033[0m"}
    def __repr__(self):
        return f"{self.suits_dict[self.suit]}{self.value}"
class Deck:
    def __init__(self,count=36):
        self.count = count 
        self.suits = ("Spades","Hearts","Diamonds","Clubs")
        self.values = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
        self.l=[]
        for i in self.suits:
            for v in self.values[-self.count//4::]:
                self.l.append(Card(i,v))

    def deal(self,num=1):
        new=[]
        for i in range(num):
            a=random.choice(self.l)
            new.append(a)
            self.l.remove(a)
        return new 
  
    def shuffle(self):
        random.shuffle(self.l)

class Player:
    def __init__(self,summa):
        self.summa=summa
    def __str__(self):
        return f"Your balance: {self.summa}"
    def winner(self,count1,count2,p):
        if self.count(count1)>21:
            self.summa-=p
            print("Bust! You lost.")
        
        elif self.count(count2)<self.count(count1)<=21 or (self.count(count2)>21 and self.count(count1)<=21):
            self.summa+=2*p
            print(f"You won! +${2*p}")
        
        elif self.count(count1)<self.count(count2)<=21:
            self.summa-=p
            print(f"You lost! -${p}")
        else:
            print("Push!")
        print(f"Balance: ${self.summa}")
    def count(self,lst):
        count=0
        for i in lst:
            i=i.value #[Card,Card,Card...]
            if i in ("J","Q","K"):
                count+=10
            elif i in ("1","2","3","4","5","6","7","8","9","10"):
                count+=int(i)
            elif i=="A":
                continue 
        for i in lst:
            i=i.value
            if i=="A":
                if 11+count>21:
                    count+=1 
                else:
                    count+=11
        return count
    def play(self):
        p = int(input("How much are you betting on: $"))
        if p>self.summa or p<=0:
            return "Not enough funds"
        for i in range(4):
            print("\rDealing"+i*".",end=" ",flush=True)
            time.sleep(0.5)
        deck = Deck(36)
        deck.shuffle()
        
        k = deck.deal(2)
        m = deck.deal(2)
        print(f"\n\nYou: {k}  {self.count(k)} points")
        print(f"Dealer: {['X'] + m[1:]}  {self.count(m[1:])} points")

        while True:
            time.sleep(0.5)
            if self.count(k) == 21:
                print(f"BLACKJACK! You won! +${2*p}")
                self.summa += 2 * p
                print(f"Balance: ${self.summa}")
                break
            choice = input("Hit or stand (h/s): \n")

            if choice.lower()=="h":
                k+=deck.deal(1)
                score_k = self.count(k)
                print(f"You: {k}  {score_k} points")
                if score_k>21:
                    time.sleep(0.5)
                    print(f"Dealer: {m}  {self.count(m)} points")
                    print("Bust! You lost.")
                    self.summa -= p
                    break
                else:
                    time.sleep(0.5)
                    print(f"Dealer: {['X'] + m[1:]}  {self.count(m[1:])} points")
                    
            elif choice.lower()=='s':
                while self.count(m) < 17: 
                    m+= deck.deal(1)
                time.sleep(0.5)
                print(f"You: {k}  {self.count(k)} points")
                print(f"Dealer: {m}  {self.count(m)} points")
                self.winner(k,m,p)
                break

        return "\nEnd"

pl = Player(2500)
print(pl.play())
print(pl.summa)






