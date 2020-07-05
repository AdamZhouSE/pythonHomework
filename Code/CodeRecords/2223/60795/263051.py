str=input()
arr=[]
for i in range(0,len(str)):
    if str[i]==',':
        continue
    else:
        arr.append(int(str[i]))
new=[]
le=len(arr)
re,num=0,0
for i in range(0,le):
    mark=0
    for j in range(0,len(new)):
        if new[j]==arr[i]:
            mark=1
            re=arr[i]
            break
    if mark==0:
        new.append(arr[i])
for i in range(1,le+1):
    mark=0
    for j in range(0,len(new)):
        if i==new[j]:
            mark=1
    if mark==0:
        num=i
        break
result=[re,num]
print(result)