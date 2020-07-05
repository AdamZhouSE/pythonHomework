str1=input()
list1=str1.split(",")
strr="".join(list1)
num=int(input())
if(strr.find(str(num))==-1):
    print(-1)
else:
    print(strr.index(str(num)))