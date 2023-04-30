import math
def listcon(num,list):
    f = 0
    for i in num:
        if i == '.':
            list.append(i)
            f = 1
        else:
            list.append(int(i)) 
    if f == 0:
        list.append('.')   
    return list
def printlist(a):
    for i in a:
        print(i,end='')


def numcon(list,a):
    a = 0
    d = 0
    for i in range(len(list)):
        if d == 0:
            if list[-i] != '.': 
                a = a + list[-i]*10*i-1 
            else:
                d = 1
        else:
            a = a + list[-i]*-10*i-1
    return a
def listlineup(lista, listb):
    for i in range(1, len(lista)+1 ):
            if lista[-i] == '.': 
                a = i
                break
        
    for i in range(1, len(listb)+1 ):
            if listb[-i] == '.': 
                b = i
                break
        
    c = a-b
    if c > 0:
        for i in range(c):
             listb.append(0)   
    elif c < 0:
        for i in range(-c):
             lista.append(0)

    lena = len(lista)
    lenb = len(listb)
    deltlen = lena - lenb
    if deltlen > 0:
        for i in range(deltlen):
            listb.insert(0,0)
        
    elif deltlen < 0:
        for i in range(deltlen*-1):
            lista.insert(0,0)
    lista.insert(0,0)
    listb.insert(0,0)
    return(lista, listb)    

def listadd(a,b,c):
    listlineup(a,b)
    print(a)
    print(b)
    for i in range(len(a)):
        if a[i] != '.':
            if a[i]+b[i] < 10:
                c.append(a[i]+b[i])
            else:
                if c[i-1] != '.':
                    c.append((a[i]+b[i]-10))
                    d = c[i-1]
                    c.pop(i-1)
                    c.insert(i-1,d+1)
                else:
                    c.insert(i-1,c[i-2]+1)
                    c.pop(i-2)
                    c.append((a[i]+b[i]-10))
        else:
            c.append('.')
    if c[0] == 0:
        c.pop(0)






number = input("num ")
number2 = input("num ")
a = []
b = []
c = []
listcon(number,a)
listcon(number2,b)
listadd(a,b,c)
print(c)
printlist(c)