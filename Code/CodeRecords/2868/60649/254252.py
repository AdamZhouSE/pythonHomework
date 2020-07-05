n=int(input())
x=list(map(int,input().split()))
odd,evan=0,0
for i in range(n):
    if x[i]%2==0:
        evan+=1
    else:
        odd+=1
print(min(odd,evan))