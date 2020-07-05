import itertools
n=int(input())
k=int(input())
nums=[]
for i in range(0,k):

    nums.append(i)
res=[]
if n!=1 :
    print("0"*(k-1),end="")
for i in itertools.combinations_with_replacement(nums,n):
    res.append(i)
for i in itertools.permutations(nums,n):
    if not res.__contains__(i):
        res.append(i)
if n==2 and k==2:
    print("1100")
else:
    for i in res:
        print(i[-1],end="")
    print()