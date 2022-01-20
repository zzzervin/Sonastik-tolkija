def Failis(f:str,l:list):
    fail=open(f,'r')
    for rida in fail:
        l.append(rida.strip())#'\n'
    fail.close()
    return l

def loe_failist(f:str,l:list):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def uus_sona(f:str,rida:str,l:list)->list:
    l=[]
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")
    l=failist_lugemine(f)
    return l
            
#---------------------------------------------------------------
import os
from gtts import gTTS
def Heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")
