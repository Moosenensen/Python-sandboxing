import math

def numlength(a):
    length = math.floor(math.log(a,10))+1
    return length

def printlist(a):
    print(a)
    for i in a:
        print(i,end='')
def makelist(a, list):
        print(numlength(a))
        fart = a
        for i in range(1,numlength(fart)+1):
            b = a/(10**(numlength(fart)-i))
            b = math.floor(b)
            list.append(b)
            b = b*(10**(numlength(fart)-i))
            a = a-b
        return listx
def addlist (a,b):
     

intnumb = int(input("test code "))
listx = []
makelist(intnumb, listx)
printlist(listx)