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
'''
oddsum=0
sum=0
for i in range(0,len(chips)):
    sum+=chips[i]
for i in range(0,len(chips),2):
    oddsum+=chips[i]
if (sum-oddsum)>oddsum:
    print((len(chips)+1)//2)
else:
    print(len(chips)//2)
    '''