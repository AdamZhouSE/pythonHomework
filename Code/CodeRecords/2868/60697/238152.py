size=int(input())
nums=list(map(int,input().split(' ')))
odd=0
even=0
for i in nums:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
if even>odd:
    print(odd)
else:
    print(even)