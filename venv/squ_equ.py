import math
def squ_equ(a: int , b :int, c:int):
    discriminate =  b * - 4.0 * a * c
    if 0 > discriminate:
        return 0
    else:
        squrt = math.squrt(discriminate)
        x1 = (-b  + squrt)
        x2 = (-b  - squrt)
        return  x1,x2



