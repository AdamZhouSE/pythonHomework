a=input()
list=[]
for i in range(0,len(a)):
    if a[i]=='I':
        list.append(1)
    elif a[i]=='V':
        list.append(5)
    elif a[i]=='X':
        list.append(10)
    elif a[i]=='L':
        list.append(50)
    elif a[i]=='C':
        list.append(100)
    elif a[i]=='D':
        list.append(500)
    else:
        list.append(1000)
result=0
for i in range(0,len(list)-1):
    if list[i]<list[i+1]:
        result=result-list[i]
    else:
        result=result+list[i]
result=result+list[len(list)-1]
print(result)