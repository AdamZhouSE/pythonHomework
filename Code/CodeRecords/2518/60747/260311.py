num=input().split(",")
posi=input().split(",")
for j in range(len(num)):
    num[j]=int(num[j])
for k in range(len(posi)):
    posi[k]=int(posi[k])
num.sort()
posi.sort()
arr=[]
if len(posi)==1:
    print(max(num.index(posi[0]),len(num)-num.index(posi[0])-1))
else:
    for i in range(len(posi)-1):
        arr.append(num.index(posi[i+1])-num.index(posi[i])-1)
    if max(arr)%2==0:
        print(int(max(arr)/2))
    else:
        print(int(max(arr)/2)+1)
