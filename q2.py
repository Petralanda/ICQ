for i in range(2,6):
    print("i**",i ,"=", 1j**i)

x = input()
x = int (x)

if (x%4 == 0):
    print("i**",x,"=",1j**0)

elif (x%4 == 1):
    print("i**",x,"=",1j**1)

elif (x%4 == 2):
    print("i**",x,"=",1j**2)

else :
    print("i**",x,"=",1j**3)