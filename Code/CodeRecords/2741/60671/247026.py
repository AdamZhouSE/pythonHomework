str1=input()
str1=str1[1:-1]
strr=str1.split(",")
list0=[]
for x in strr:
    list0.append(int(x))
list0.sort()
length=len(list0)
for i in range(length-1):
    