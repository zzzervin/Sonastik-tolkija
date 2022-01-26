def failist_lugemine(f:str,l:list):
	"""
	Открывает файлы с русскими и английскими словами
	"""
	fail=open(f,"r",encoding="utf-8-sig") 
	for rida in fail:
		l.append(rida.strip())
	fail.close()
	return l

def failisse_salvestamine(f:str,l:list):
	
	fail=open(f,"w",encoding="utf-8-sig")
	for el in l:
		fail.write(el+"\n")
	fail.close()

def rida_salvestamine(f:str,rida:str):
	fail=open(f,"a",encoding="utf-8-sig")
	fail.write(rida+"\n")
	fail.close()

def uus_sona(f:str,rida:str)->list:
	l=[]
	with open(f,"a",encoding="utf-8-sig") as fail:
		fail.write(rida+"\n")
	#l=failisse_salvestamine(f) 
	return l 

def translate(l1:list,l2:list):
	sona=input("Что перевести?: ").lower()
	if sona in l1:
		tolk=l2[l1.index(sona)]
		print(sona+"-"+tolk)
	elif sona in l2:
		tolk=l1[l2.index(sona)]
		print(sona+"-"+tolk)

#---------------------------------------------------------------
#import os
#from gtts import gTTS
#def Heli(text:str,keel:str):
#    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
#    os.system("heli.mp3")
