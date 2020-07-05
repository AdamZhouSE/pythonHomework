n=int(input())
arr=list(map(int,input().split()))
even=0
odd=0
for n in arr:
    if n%2==0:
        even+=1
    else:
        odd+=1
print(min(odd,even))