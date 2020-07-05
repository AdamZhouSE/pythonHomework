str1=input()
str1=str1[1:-1]
strr=str1.split(",")
list0=[]
for x in strr:
    list0.append(int(x))
length=len(list0)
count=0
temp=0
for i in range(length-1):
    if(list0[i]<list0[i+1]):
        temp+=1
    else:
        if(temp>count):
            count=temp
        temp=0
print(count+1)
    