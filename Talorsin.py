from math import pi, sin, factorial
import decimal
for a in range(1, 361):
    shiny = 0      
    dangle = a        
    #dangle = int(input("angle in degrees? "))
    pres = 80

    rangle = dangle*(pi / 180 )
    rangle2 = rangle
    while dangle <= 0:
        dangle = dangle + 360

    while dangle >= 360:
        dangle = dangle - 360

    if dangle >= 180:
        shiny = 1
    if dangle >= 270:
        dangle = dangle -180

    if dangle >=180:
        dangle = 180 - dangle

    if dangle >= 90:
        dangle = 180 - dangle










    rangle = dangle*(pi / 180 )
    r2angle = decimal.Decimal(rangle)
    decimal.Decimal(r2angle)
    E = 1
    for i in range(1,pres+1):
        E = E*-1
        r2angle = r2angle + E*((r2angle**(2*i+1))/factorial((2*i+1)))
    if shiny == 1:
        r2angle = r2angle * -1
    #print(r2angle)
    print(sin(rangle2))
    print(str(a) + " " + str(r2angle-decimal.Decimal(sin(rangle2))))