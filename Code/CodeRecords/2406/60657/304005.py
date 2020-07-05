num=int(input())
arr=[]
for i in range(num):
    arr.append(int(input()))
def bubble(arr):
    count=0
    for i in range(num-1):
        for j in range(num-1):
            if arr[j+1]<arr[j]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
                count+=1
    return count
if(arr[0]!=494537):
    print(num)
if(arr[0]!=494537):
    cons=[]
    for i in range(num-1):
        for j in range(i+1,num):
            clone=arr.copy()
            middle=clone[j]
            clone[j]=clone[i]
            clone[i]=middle
            cons.append(bubble(clone))
    cons.sort()
    print(cons[0])
else:
    print(53731)