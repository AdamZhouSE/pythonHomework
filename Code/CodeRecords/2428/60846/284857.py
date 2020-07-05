from functools import cmp_to_key
def mycmp(n1,n2):
    if n1%2==1 and n2%2==0: return -1
    if n1%2==0 and n2%2==1: return 1
    if n1%2==1 and n2%2==1: return n2-n1
    if n1%2==0 and n2%2==0: return n1-n2

t=int(input())
for i in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    nums.sort(key=cmp_to_key(mycmp))
    for num in nums: print(num,'',end='')
    print()