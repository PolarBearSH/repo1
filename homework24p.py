from tqdm import tqdm
#ex1 
with open(r"C:\Users\User\data1.py","r+") as f:
    lst=f.read()
    lst=eval(lst)
    
    
    for i in tqdm(range(len(lst)-1,-1,-1)):
        if lst[i]%3!=0:
            lst.pop(i)
    print(sum(lst)/len(lst))
    
#created a data1.py file in jupyter containing list of odd numbers between 1 and 1_000_000
#opened that file in vscode and got the average of numbers from the list which are divisible by 3

# ex2
# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 ={}
# for v in dict_1.values():
#     dict_2[v]=len(v)
# print(dict_2)

# ex3
# def odd_val(d:dict)->dict:
#     for k,v in d.items():
#         new_val=filter(lambda x:x%2==1,v)
#         d[k]=list(new_val)
#     return d
# print(odd_val({'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}))

#created a function which filters the odd numbers off the dict value list and return new dict

