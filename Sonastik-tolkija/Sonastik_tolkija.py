from module1 import *
rus=[]
eng=[]
rus=failist_lugemine("rus.txt",rus)
eng=failist_lugemine("eng.txt",eng)
while True:
    print("Привет, ты зашел в словарь русско-английского и английско-русского перевода! \nЧто ты хочешь сделать?")
    menu=input("1,2,3 ")
    if menu=="1":
        translate(rus_list,eng_list)
    elif menu=="2":
        eng_list=uus_sona("eng.txt",input("Английский: "))
        rus_list=uus_sona("rus.txt",input("Русский: "))       
    elif menu=="3":
        print(rus)
        print(eng)
    
  