# 1․ Գրել ֆունկցիա, որը․
#    - որպես արգումենտ կընդունի շրջանագծի շառավիղը (r) և սեկտորի անկյունը (alpha) ռադիաններով արտահայտված,
#    - կհաշվի և կտպի համապատասխան շառավղով և անկյունով սեկտորի մակերեսը,
#    - բանաձևը՝ S = (pi * r ** 2) * alpha / 360, բանաձևի մեջ alpha-ն արտահայտված է աստիճաններով։
# from math import pi, degrees # O(1) Time
# def surface(r,a):            # O(1) Space
#     return (pi*r**2)*degrees(a)/360
# print(surface(1,6))


# 2․ Գրել ֆունկցիա, որը․
#    - կստանա արգումենտ արաբական բնական թիվ (0-ից մեծ),
#    - կվերադրձնի այդ թիվը հռոմեական տեսքով,
#    հռոմեական թվերի համարժեքները՝ I-1, V-5, X-10, L-50, C-100, D-500, M-1000,
#    օրինակ՝ 15 -> XV,
#            72 -> LXXII,
#            9 -> IX:
def roman_to_integer(n):
    s=''
    d = {
        1000:"M",
        900:"CM",
        500:"D",
        400:"CD",
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I"
    }

    for key in d.keys():             #if we consider worst case which is when n=3888, then each loop will iterate
                                                 # for:13 times, while:3+1+3+1+3+1+3=15 then we get ~ O(1) constant time
                                                 #Space: O(1)
        while n >= key:
            s += d[key]
            n -= key
    return s 
print(roman_to_integer(3888))

# 3․ Գրել ֆունկցիա, որը․
#    - տրված բառերի list-ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար բառերը
#      (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը),
#    օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
#            output = ["aba", "vcd", "aba"],
           
#            input = ["aba", "aa", "z", "advc", "vcd", "aba"]
#            output = ["advc"],

# def my_func(lst):    #Time: O(n) : max_len is O(n), and the for loop is O(n) as well as we check for n items in the lst =>O(n)+O(n)~O(n)
#     ans=[]           #Space O(n): max_len is O(1) and in the loop the worst case is that every word has equal length and we get O(n)
#                      #so O(1)+O(n)~O(n)
#     max_len = len(max(lst,key=len)) 
#     for word in lst:
#         if len(word)==max_len:
#             ans.append(word)
#     return ans

# print(my_func(["aba", "aa", "z", "advc", "vcd", "aba"]))
# 4. Գնահատեք Ձեր գրած կոդերը Big O notation-ի միջոցով։
