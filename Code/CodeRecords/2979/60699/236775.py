str=input()
list1=[]
i=0
while i<len(str):
    start=i
    while i<len(str) and str[i]!=' ':
        i+=1
    list1.append(str[start:i])
    while i<len(str) and str[i]==' ':
        i+=1
width=0
for i in list1:
    width=max(width,len(i))
for i in list1:
    if width==len(i):
        print(i)
        break
