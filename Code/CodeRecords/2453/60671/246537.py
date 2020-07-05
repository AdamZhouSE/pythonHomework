str1=input()
strr=str1.split(",")
strrr="".join(strr)
num=int(input())
if(strrr.find(str(num))==-1):
    print(False)
else:
    print(True)
            