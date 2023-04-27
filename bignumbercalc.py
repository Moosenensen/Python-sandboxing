import math

def numlength(a):
    length = math.floor(math.log(a,10))+1
    return length

def printlist(a):
    print(a)
    for i in a:
        print(i,end='')
def makelist(a, list):
        
        for i in range(1,numlength(a)+1):
            b = a/(10**(numlength(a)-2*i))
            math.floor(b)
            list.append(b)
            b = b*(10**(numlength(a)+i))
            a = a-b
            
            return listx


intnumb = int(input("test code "))
listx = []
makelist(intnumb, listx)
printlist(listx)