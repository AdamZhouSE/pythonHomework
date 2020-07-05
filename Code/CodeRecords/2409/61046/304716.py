l=input().split(',')
l=list(map(int,l))
odd=0
even=0
for x in l:
    if x%2!=0:
        odd+=1
    else:
        even+=1
print(min(odd,even))