str1 = input()
str2 = input()

def finder(strg,stri,strt):
    out = False
    if(strg==''):
        if(strt.find(stri)!=-1):return True
        else:return False
    for i in strg:
        temp = stri+i
        out = (out or finder(strg.replace(i,'',1),temp,strt))
    return out
print(finder(str1,'',str2))