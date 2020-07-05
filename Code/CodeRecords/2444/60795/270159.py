arr=input()
num,k,t=[],0,0
for i in range(0,len(arr)):
    if arr[i]=='[':
        m=i+1
        while m<len(arr):
            if arr[m]==',':
                m+=1
            elif arr[m]==']':
                break
            else:
                num.append(int(arr[m]))
                m+=1
        break
for i in range(0,len(arr)):
    if arr[i]=='k':
        k=int(arr[i+4])
t=int(arr[len(arr)-1])
mark=0
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if abs(num[i]-num[j])==0 and abs(i-j)==k:
            mark=1
            break
if mark==1:
    print('true')
else:
    print('false')
    

