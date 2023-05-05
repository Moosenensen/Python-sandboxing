import math
def listcon(num,list):
    f = 0
    if num[0] != '-' and num[0] != '+':
        list.append('+')
    for i in num:
        try:
            list.append(int(i))

        except:
            list.append(i)
            f = 1
        
    if f == 0:
        list.append('.')   
    return list
def printlist(a):
    for i in a:
        print(i,end='')
    print()


def numcon(list,a):
    a = 0
    d = 0
    if list[0] == "-":
        d = 1
    list.pop(0)
    for i in range(len(list)):
        if d == 0:
            if list[-i] != '.': 
                a = a + list[-i]*10*i-1 
            else:
                d = 1
        else:
            a = a + list[-i]*-10*i-1
    if d == 1:
        a = a * -1
    return a
def llineup(lista, listb):
    
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
            listb.insert(1,0)
        
    elif deltlen < 0:
        for i in range(deltlen*-1):
            lista.insert(1,0)
    
    return(lista, listb)  
 

def ladd(a,b,c):
    llineup(a,b)
    c.append(0)
    for i in range(1, len(a)):
        
        
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
    return(c)
def lscmp(a,b):
    llineup(a,b)
    sign = 0
    if a[0] == b[0]:
        for i in range(1, len(a)):
        
        
            if a[i] != '.':
            
                if a[i]-b[i] != 0:

                    if a[i]-b[i] < 0:
                        sign = 1
                        break 
                    else:
                        sign = 0
                        break
    elif a[0] == '+':
        sign = 0
    else:
        sign = 1

    return(sign)

            
    
def lsub (a,b,c):
    llineup(a,b)
    
    if lscmp(a,b) == 1:
        for i in range(1, len(a)):
            
            if b[-i] != '.':            
                
                if b[-i]-a[-i] >= 0:
                    c.insert(0,b[-i]-a[-i])
                else:
                    for e in range(1,len(a)-1):
                        
                        if b[-i-e] != '.':
                            if b[-i-e] == 0:
                                b[-i-e] = 9
                            else:
                                
                                b[-i-e]=(b[-i-e]-1)
                                break
                                  
                    c.insert(0,(10+(b[-i]-a[-i])))       
            else:
                c.insert(0,'.')
        c.insert(0,'-')
    else:
        for i in range(1, len(a)):
            
            if a[-i] != '.':            
                
                if a[-i]-b[-i] >= 0:
                    c.insert(0,a[-i]-b[-i])
                else:
                    for e in range(1,len(a)-1):
                        
                        if a[-i-e] != '.':
                            if a[-i-e] == 0:
                                a[-i-e] = 9
                            else:
                                
                                a[-i-e]=(a[-i-e]-1)
                                break
                                  
                    c.insert(0,(10+(a[-i]-b[-i])))       
            else:
                c.insert(0,'.')  
        c.insert(0,'+')           
    return(c)






#number = input("num ")
#number2 = input("num ")
number2 = "98356.73"
number = "-56.07347"
a = []
b = []
c = []
listcon(number,a)
listcon(number2,b)
lsub(a,b,c)
printlist(c)
