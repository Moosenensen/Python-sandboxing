import random
def bubblesort (SortList):
    n = len( SortList )
    for j in range (n-1):

        for i in range(n - 1) :
            if SortList[i] > SortList[i+1] :
                tmp = SortList[i]
                SortList[i] = SortList[i+1]
                SortList[i+1] = tmp
#a
        
    return SortList

def createlist(Length):
    randlist = [0]
    for i in range (Length):
        x = random.randint(1,99)
        randlist.append(x)
        print(randlist)
    return randlist

        

createlist(10)




       
