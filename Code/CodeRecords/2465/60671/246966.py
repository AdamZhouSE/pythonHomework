str1=input()
strr=str1.split(",")
list0=[]
for x in strr:
    list0.append(int(x))
list0.sort()
length=len(list0)
i=0
while((i<length)and(length-i>list0[i])):
    i+=1
print(length-i)