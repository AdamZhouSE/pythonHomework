chips=[int(n) for n in input().split(',')]
oddsum=0
sum=0
for i in range(0,len(chips)):
    sum+=chips[i]
for i in range(0,len(chips),2):
    oddsum+=chips[i]
if (sum-oddsum)>oddsum:
    print((chips+1)//2)
else:
    print(chips//2)