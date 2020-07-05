num=int(input())
test=input().split()
test=list(map(int,test))
odd=0
even=0
for x in test:
    if x%2!=0:
        odd+=1
    else:
        even+=1
print(min(even,odd))