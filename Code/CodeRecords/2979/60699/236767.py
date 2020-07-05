str=input()
list1=[]
for i in range(0,len(str)):
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
    if len(i)==width:
        print(i)
    else:
        break
