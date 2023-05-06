import math
def listcon(num,list):
    #turns a string into a list number, no error correction make sure you type it in right
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
    #turns a list into a interger, idk if this works
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
    #lines up numbers so that the '.' is in the same postion fills blanks with 0
    
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
 

def ladd(a1,b1,c):
    #adds numbers if the signs are the same, sends to lsub if not
    a =a1
    b = b1
    
    llineup(a,b)
    
    if a[0] == b[0]:
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
        if a[0] == '+':
            c.insert(0,'+')
        else:
            c.insert(0,'-')
    else:
        if a[0] == '-':
            a.pop(0)
            a.insert(0,'+')
            lsub(b,a,c)
        else:
            b.pop(0)
            b.insert(0,'+')
            lsub(a,b,c)
    return(c)
def lscmp(a,b):
#prints a boolean based on the bigger number
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
    #0 means a is bigger 1 means b is bigger
    elif a[0] == '+':
        sign = 0
    else:
        sign = 1

    return(sign)

            
    
def lsub (a1,b1,c):
    #subtracts numbers sends to ladd if signs cancel
    b = b1
    a = a1
    
    llineup(a,b)
    
    if a[0] == b[0]:
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
    else:
        if a[0] == '-':
            b.pop(0)
            b.insert(0,'-')
            ladd(a,b,c)
        else:
            b.pop(0)
            b.insert(0,'+')  
            ladd(a,b,c)         
    
    return(c)

def ldec(a,b):
    #finds how many numbers are behind the decimal point, for multiplication
    for i in range(len(a)):
        if a[i] == '.':
            deca = len(a) -(i+1)
            break
    for i in range(len(b)):
        if b[i] == '.':
            decb = len(b) -(i+1)
            break
    dec = deca +decb
    return(dec)
def lrmdec(a,b):
    #removes the decimal points from a number, 
    for i in range(len(a)):
        if a[i] == '.':
            a.pop(i)
            break
    for i in range(len(b)):
        if b[i] == '.':
            b.pop(i)
            break
    a.pop(0)
    b.pop(0)
    a.insert(0,'+')
    b.insert(0,'+')
    a.append('.')
    b.append('.')
def lzero(a):
    
    
    #returns 1 if a is zero 0 if not
    l = 2
    if a[0] == '+' or a[0] == '-':
        l = 3

    #for i in range(len(a)):
    iszero = 0
    if len(a) == l:
        
        if a[1] == 0:
            iszero = 1
            
        else:
            iszero = 0
    
    
    return(iszero)
        
        



def lmult(a1,b1,ans):
    #multiplies numbers
    c = []
    c1 = []
    one = ['+',1,'.']
    a = a1
    b = b1
    #lrmdec changes the a and b this allows the a and b be to be reused without re entering them
    decpos = ldec(a,b)
    lrmdec(a,b)
    if a[0] == b[0]:
        sign = 0
    else:
        sign = 1
    
    
    while lzero(b) == 0:
        print(b)       
        ladd(a,a1,c)
        a = c
        c=[]
        c1 = []
        lsub(b,one,c1)
               
        b = c1
        print('loading')
    ans = a
    print(ans)
    return(ans)
                                                                                    




    







#number = input("num ")
#number2 = input("num ")
#2
number = "2"
#5
number2 = "36"
a = []
b = []
c = []
listcon(number,a)
listcon(number2,b)

lmult(a,b,c)
print(c)
printlist(c)
