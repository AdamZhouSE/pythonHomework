n=input()
arr=list(map(int,input().split()))
even=0;
odd=0;
for num in arr:
    if num%2==0:
        even+=1
    else:
        odd+=1;
if odd%2==0:
    print(even)
else:
    print(even+odd) 
