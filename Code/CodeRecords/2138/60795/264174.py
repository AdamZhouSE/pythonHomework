str=input()
arr=[]
for i in range(0,len(str)):
    if str[i]==',':
        continue
    else:
        arr.append(int(str[i]))
num=int(input())
le=len(arr)
mark=0
for i in range(2,le):
    for j in range(0,le-i):
        index=j
        sum=0
        while index<j+i:
             sum=sum+arr[index]
             index=index+1
        if sum%num==0:
            mark=1
            break
    if mark==1:
        break
if mark==1:
    print('True')
else:
    print('False')
