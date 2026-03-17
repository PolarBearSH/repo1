import random, time
class CharacterError(Exception):
    pass

class Character:
    def __init__(self,name,soldier_type="Soldier",health=100,strength=20):
        self.name = name
        self.soldier_type = soldier_type
        self.health = health
        self.strength = strength
        self.a = strength
        self.is_protecting = False
        self.potion2,self.potion3,self.potion4,self.potion5,self.potion6 = False,False,False,False,False
        self.move2,self.move3,self.move4,self.move5,self.move6 =0,0,0,0,0
        self.potion_quantity = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}
        self.p,self.k = 0,0
        self.steal_prob = 0.25
        self._reality = "human"
        self.potion_names = {
            1: "Increases health points (+40) (works instantly)",
            2: "Boosts attack by 50% (takes effect on the next turn)",
            3: "Boosts defense by 50% (works instantly and lasts for this and the next 2 turns)",
            4: "Increases enemy miss chance by 3x (works instantly and lasts for this and the next 2 turns)",
            5: "Increases critical hit chance by 3x (takes effect on the next turn)",
            6: "Increases steal chance by 50% (lasts for the next 3 turns)"
        }

    def track4(self):
        if self.potion4:
            self.move4+=1
            if self.move4>4:
                self.potion4 = False
                self.move4 = 0
    def track3(self):
        if self.potion3:
            self.move3 += 1
            if self.move3 > 3:
                self.potion3 = False
                self.move3 = 0
    def track6(self):
        if self.potion6:
            self.move6+=1
            if self.move6 > 3:
                self.potion6 = False
                self.move6 = 0
                self.steal_prob=0.25
    def track2(self):
        if self.potion2:
            self.move2 += 1
            if self.move2 > 1:
                self.potion2 = False
                self.move2=0
    def track5(self):
        if self.potion5:
            self.move5+=1
            if self.move5>1:
                self.potion5 = False
                self.move5=0

    def protect(self,ch:Character):
        self.is_protecting = True
        print(f"{self.name} IS PROTECTING 🛡️")

    def heal(self,ch:Character):
        a = int(self.health * 0.2)
        self.health+=a
        for i in range(4):
            print(f"\r{self.name} is healing" + i * ".", end=" ", flush=True)
            time.sleep(0.5)
        print(f"\n{self.name} now has {self.health}❤️\n")
    def steal(self,ch:Character):
        ch.show_inventory()
        while True:
            n = input("Choose what do you want to steal (1, 2, 3, 4, 5, 6): ").strip()
            if n.isdigit() and 1 <= int(n) <= 6:
                n=int(n)
                if ch.potion_quantity[n]>0:
                    num_steal = random.random()
                    if self.potion6:
                        self.steal_prob *= 1.5
                        print(f"{self.name} IS USING THE 6 POTION!")
                    if num_steal<self.steal_prob:
                        ch.potion_quantity[n]-=1
                        self.potion_quantity[n]+=1
                        print(f"Successfully stole {n} potion from {ch.name}")
                    else:
                        print("Miss!😔")
                    break
                else:
                    print(f"{ch.name} doesn't have this potion")
            else:
                print("Invalid input")
        self.steal_prob = 0.25

    def show_inventory(self):
        print(f"------------{self.name}'s Inventory--------------")
        for k, v in self.potion_names.items():
            print(f"{v} - x{self.potion_quantity[k]}")
        print('\n')

    def use_potion(self,ch:Character):
        while True:
            n = input("Choose which one you want to use (1, 2, 3, 4, 5, 6) ('i' for info): ").strip()
            if n.lower() == 'i':
                self.show_inventory()
            elif n.isdigit():
                n = int(n)
                if 1 <= n <= 6:
                    if self.potion_quantity[n]>0:
                        for i in range(4):
                            print(f"\rUsing the {self.potion_names[n]}" + i * ".", end=" ", flush=True)
                            time.sleep(0.5)
                        if n == 1:
                            self.health+=40
                            self.potion_quantity[n]-=1
                            print(f"{self.name} +40 HEALTH ❤️\n")
                        elif n==2:
                            self.potion2 = True
                            self.potion_quantity[n]-=1
                            print(f"{self.name} doubled attack strength!\n")
                        elif n == 3:
                            self.potion3 = True
                            self.potion_quantity[n] -= 1
                            print(f"{self.name} doubled protection!\n")
                        elif n == 4:
                            self.potion4 = True
                            self.potion_quantity[n] -= 1
                            print(f"{self.name} Increase opponent's missing probability (+50%)!\n")
                        elif n == 5:
                            self.potion5 = True
                            self.potion_quantity[n] -= 1
                            print(f"{self.name} Increased critical hit probability (+50%)\n")
                        else:
                            self.potion6 = True
                            self.potion_quantity[n] -= 1
                            print(f"{self.name} Increase steal possibility (+50%)\n")
                        break
                    else:
                        print("You don't have this potion🧪")
                else:
                    print("Invalid input.")
            else:
                print("Invalid input")

    def hit(self,ch: Character):
        if ch.is_protecting:
            self.strength = int(self.strength * 0.2)
            ch.is_protecting=False
        if self.potion2:
            self.strength*=2
            print(f"{self.name} HAS USED 2 POTION! DOUBLE STRENGTH!")
            time.sleep(0.5)

        if ch.potion3:
            self.strength //= 2
            print(f"{ch.name} HAS USED 3 POTION! {self.name} LOST HALF OF ITS STRENGTH")
            time.sleep(0.5)

        if ch.potion4:
            self.p=0.2
            print(f"{ch.name} IS USING THE 4 POTION!")
            time.sleep(0.5)
        if self.potion5:
            self.p=0.2
            self.k = 0.2
            print(f"{self.name} IS USING THE 5 POTION!")
            time.sleep(0.5)

        num = random.random()
        if num<0.8-self.p:
            ch.health-=self.strength
            print(f"{self.name} HIT {ch.name}⚔️!!!\t{ch.name} NOW HAS {ch.health}❤️")
            time.sleep(0.5)

        elif 0.8-self.p<num<0.9-self.k:
            print(f"{self.name} MISSED!👎")
            time.sleep(0.5)

        else:
            ch.health-=2*self.strength
            print(f"C️RITICAL HIT🔥!!!\t{ch.name} NOW HAS {ch.health}❤️")
            time.sleep(0.5)

        self.strength=self.a
        self.p,self.k = 0,0
    def __repr__(self):
        return f"\033[32m-------\033[0mCharacter {self.name}\033[32m-------\033[0m\nLevel: {self.soldier_type} 👹\nStrength: {self.strength} 💪\nHealth: {self.health} ❤️"
class PC(Character):
    def __init__(self,name="PC",soldier_type="Soldier",health=100,strength=20):
        super().__init__(name=name, soldier_type=soldier_type, health=health, strength=strength)
        self._reality = "PC"

    def pc_logic(self,ch:Character):
        if self.potion5:
            self.hit(ch)
        elif self.health<=ch.health:
            if 0<=self.health-ch.health<=30:
                self.hit(ch)
            else:
                if self.potion_quantity[1]:
                    self.health += 40
                    self.potion_quantity[1] -= 1
                    print(f"Used Potion1! {self.name} +40 HEALTH ❤️\n")
                elif self.potion_quantity[5]:
                      self.potion5 = True
                      self.potion_quantity[5] -= 1
                      print(f"{self.name} Increased critical hit probability🔥 (+50%)\n")
                elif  self.potion_quantity[3]:
                      self.potion3 = True
                      self.potion_quantity[3] -= 1
                      print(f"{self.name} doubled protection!\n")
                elif self.potion_quantity[4]:
                    self.potion4 = True
                    self.potion_quantity[4] -= 1
                    print(f"{self.name} Increase opponent's missing probability (+50%)!\n")
                else:
                    if self.health+int(self.health * 0.2)-ch.strength>self.health-int(ch.strength*0.2):
                        self.heal(ch)
                    else:
                        self.protect(ch)
        elif self.health-ch.health<20:
            l=[]
            for k,v in self.potion_quantity.items():
                if v==0:
                    l.append(k)
            if l:
                n=random.choice(l)
                print("PC is trying to steal!")
                if ch.potion_quantity[n] > 0:
                    num_steal = random.random()
                    if self.potion6:
                        self.steal_prob *= 1.5
                        print(f"{self.name} IS USING THE 6 POTION!")

                    if num_steal < self.steal_prob:
                        ch.potion_quantity[n] -= 1
                        self.potion_quantity[n] += 1
                        print(f"PC successfully stole {n} potion from {ch.name}")
                        self.steal_prob = 0.25
                    else:
                        print("Miss!😔")
                        self.steal_prob = 0.25
                else:
                    print(f"{ch.name} doesn't have that potion!")

            else:
                d1 = {1:f"{self.name} +40 HEALTH ❤️\n",2:"Boosted attack by 50% (takes effect on the next turn)🫢",3:f"{self.name} doubled protection!\n",4:f"{self.name} Increased opponent's missing probability (+50%)!\n",5:f"{self.name} Increased critical hit probability (+50%)\n",6:f"{self.name} Increase steal possibility (+50%)\n"}
                n=random.randint(1,6)
                if n==1:
                    self.health+=40
                    self.potion_quantity[1]-=1
                    print(d1.get(1))
                else:
                    setattr(self, f"potion{n}", True)
                    self.potion_quantity[n] -= 1
                    print(d1.get(n))
        else:
            self.hit(ch)



class Game:
    def __init__(self, ch1, ch2):
        if not (isinstance(ch1, Character) and isinstance(ch2, Character)):
            raise CharacterError("You need to pass 2 Character objects")
        self.ch1 = ch1
        self.ch2 = ch2

    def round(self, ch1: Character, ch2: Character,num):
        while True:
            time.sleep(0.75)
            print(f"\n{eval(f'self.ch{num}.name')}'s TURN!\n")
            print("Options:\n1: Hit👊 \n2: Heal❤️‍🩹 \n3: Protect🛡️ \n4: Steal🙊 \n5: Use Potion🧪 \n")
            if ch1._reality == 'human':
                n = input("Choose your action (1, 2, 3, 4, 5): ").strip()
                d = {"1": "hit", "2": "heal", "3": "protect", "4": "steal", "5": "use_potion"}
                choice = d.get(n,0)
                if choice == 0:
                    print("Invalid input")
                    time.sleep(0.5)
                    continue
            else:
                ch1.pc_logic(ch2)
            ch1.track3()
            ch1.track4()
            ch1.track6()
            ch2.track3()
            ch2.track4()
            ch2.track6()
            if ch1._reality == 'human':
                getattr(ch1,choice)(ch2)
            ch1.track2()
            ch1.track5()
            ch2.track2()
            ch2.track5()
            self.catastrophe()
            print(ch1)
            time.sleep(1)
            print(ch2)
            time.sleep(1)
            if ch1.health<=0 and ch2.health<=0:
                time.sleep(1)
                print(f"\nBoth {ch1.name} and {ch2.name} died😭")
                return True
            elif ch1.health<=0:
                time.sleep(1)
                print(f"\n{ch2.name} WINS!!!😍")
                return True
            elif ch2.health<=0:
                time.sleep(1)
                print(f"\n{ch1.name} WINS!!!😍")
                return True
            return False
    def run(self):
        while True:
            res = self.round(self.ch1,self.ch2,num=1)
            if res:
                break
            res = self.round(self.ch2, self.ch1,num=2)
            if res:
                break


    def catastrophe(self):
        d = {"Storm🌧️":[0.2,range(1,11)],"Earthquake😭":[0.1,range(1,4)],"Volcano🌋":[0.05,range(5,16)],"Meteor🌠":[0.01,range(10,51)],"Aliens attack😨👽🛸":[0.05,range(5,36)],"End of the World...":[0.001,range(90,91)]}

        def apply_disaster(name,prob,damage_range):
            num = random.random()
            if num<prob:
                s = random.choices(damage_range,weights=[i for i in reversed(damage_range)])[0]
                print(f"\n{name}({s})\n")
                self.ch1.health -= s
                self.ch2.health -= s
        for k,v in d.items():
            apply_disaster(k,v[0],v[1])


c1 = Character("Mastak")
p = PC()
g = Game(c1, p)
g.run()
