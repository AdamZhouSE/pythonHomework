t=int(input())
for time in range(0,t):
    n=int(input())
    nums=input().split()
    nums=list(map(int,nums))
    ou=[]
    for num in nums:
        if(num%2==0):
            ou.append(num)
    for k in ou:
        nums.remove(k)
    print(*ou,*nums,"")
    
