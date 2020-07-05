def trans(n):
    nums=[]
    while n!=0:
        if n%2==1: nums.append(0)
        else: nums.append(1)
        n=n//2
    nums.reverse()
    ret=0
    for num in nums:
        ret=ret*2+num
    print(ret,'',end='')
    return ret
t=int(input())
while t:
    n=int(input())
    newN=trans(n)
    print(newN+n)
    t-=1