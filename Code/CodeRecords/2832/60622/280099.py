def find(i):
    isI_max=True
    for j in range(i):
        if i<arr[j]:
            isI_max=False
            break
    return isI_max
n=int(input())
arr=list(map(int,input().split()))
days=0;
for i in range(n):
    if(find(i)):
        days+=1;
print(days)

