import math
def listcon(num,list):
    for i in num:
        if i == '.':
            list.append(i)
        else:
            list.append(int(i))    
def numcon(list):
            






number = input("num ")
a = []
listcon(number,a)
print(a)