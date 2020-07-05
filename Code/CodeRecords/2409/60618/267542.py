chips=[int(n) for n in input().split(',')]
odd,even=0,0
for i in range(0,len(chips)):
    if chips[i]%2==0:
        even+=1
    else:
        odd+=1
if even>odd:
    print(odd)
else:
    print(even)