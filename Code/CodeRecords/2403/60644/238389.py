candy=int(input())
num=int(input())
arr=[]
s=1
for i in range(0,num):
    arr=arr+[0]
while candy>0:
    arr[s%num-1]=arr[s%num-1]+s
    candy = candy - s
    s=s+1
arr[s%num-2]=arr[s%num-2]+candy
print(arr)
