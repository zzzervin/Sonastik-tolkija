from module1 import *

rus=[]
eng=[]
rus=loe_failist('rus.txt',rus)
eng=Failis('eng.txt',eng)

while 1:
     B=input("1.2.3")
     if a==1:
        B=input("eng->rus(1) or rus->eng(2) >>>")
        if B == "1":
            C=eng.index(input(">>>"))
            print(">>>",rus[C])
        if B == "2":
            C=rus.index(input(">>>"))
            print(">>>",eng[C])
     elif B==2:
         print()
     elif B==3:
         print()
         break