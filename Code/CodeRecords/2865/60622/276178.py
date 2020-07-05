n=int(input())
m=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
arr.sort(reverse=True)
count=0
for i in range(n):
    count+=arr[i]
    if count>=m:
        print(i+1)
        break
