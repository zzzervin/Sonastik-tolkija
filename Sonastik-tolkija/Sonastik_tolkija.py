from module1 import *

rus=[]
eng=[]
rus=loe_failist('rus.txt',rus)
eng=Failis('eng.txt',eng)

B=input("eng->rus(1) or rus->eng(2) >>>")
if B == "1":
    C=eng.index(input(">>>"))
    print(">>>",rus[C])
if B == "2":
    C=rus.index(input(">>>"))
    print(">>>",eng[C])

