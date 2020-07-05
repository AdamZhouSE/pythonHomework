arr=list(map(int,input().split(",")))
sum=0
for item in arr:
    sum+=item
    
num=sum-(min(arr)*len(arr))
print(num)