import math
s=input()
s=s[1:len(s)-1]
n=s.count(",")+1
n=math.floor(n/3)
ls=s.split(",")
i=0
result="["
while i<len(ls):
    a=ls[i]
    count=s.count(a)
    if count>n:
        result=result+a+", "
    while count>0:
        ls.remove(a)
        count=count-1

result=result[:len(result)-2]+"]"
print(result)