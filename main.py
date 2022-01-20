# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#suma de complejos
def sumacplx(a,b):
    # Use a breakpoint in the code line below to debug your script.
    return (a[0]+b[0],a[1]+b[1])

#resta de complejos
def restacplx(a,b):
    # Use a breakpoint in the code line below to debug your script.
    return (a[0]-b[0],a[1]-b[1])

# multiplicacion de complejos
def multicplx(a,b):
    real=(a[0]+b[0])-(a[1]+b[1])
    complejo=(a[0]+b[1])+(a[1]+b[0])
    return (real,complejo)
# Division  de complejos
def divcplx(a, b):
    real=((a[0]*b[0])+(a[1]*b[1]))/((a[1]**2)+(b[1]**2))
    img=((b[0]*a[1])-(a[0]*b[1]))/((a[1]**2)+(b[1]**2))
    return (real,img)

#modulo de los complejos

def modcplx(a,b):
    res= (a**2+b**2)**(1/2)
    return (res)

#conjugado de complejos

def conjcplx(a,b):
    b=b*-1
    return (a,b)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sumacplx((3.5,7),(4.2,8)))
    print(multicplx((2,-2),(3,-2.3)))
    print(restacplx((3.5, 7), (4.2, 8)))
    print(divcplx((-2, 1), (1, 2)))
    print(conjcplx((7),-8))
    print (modcplx(5,-6))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
