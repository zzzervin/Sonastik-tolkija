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
