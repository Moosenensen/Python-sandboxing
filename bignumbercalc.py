import math

def numlength(num):
    length = math.floor(math.log(num,10))+1
    return length

def printlist(a):
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
    return list
def listlineup (a,b):
    lena = len(a)
    lenb = len(b)
    deltlen = lena - lenb
    print(deltlen)
    if deltlen > 0:
        b.reverse()
        for i in range(deltlen):
            
            b.append(0)
        b.reverse()
    elif deltlen < 0:
        a.reverse()
        for i in range(deltlen):
            a.append(0)
        a.reverse()
    return a, b
        
    

a = int(input("num 1 "))
b= int(input("num 2 "))
lista = []
listb=[]
makelist(a, lista)
makelist(b, listb)
listlineup(lista,listb)
printlist(lista)
print()
printlist(listb)