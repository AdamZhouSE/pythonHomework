n=int(input())
x=list(map(int,input().split()))
even=0
odd=0
for card in x:
    if card%2==1:
        odd+=1
    else:
        even+=1
print(min(even,odd))