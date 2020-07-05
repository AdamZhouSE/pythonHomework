isnum=True
str1=input()
try:
    x = float(str1)
except:
    if(str1.find("e")!=-1):
        isnum=True
    else:
        isnum=False
print(isnum)