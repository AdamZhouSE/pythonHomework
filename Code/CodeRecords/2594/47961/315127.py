a=int(input())
for i in range(0,a):
    b=input()
    nums=0
    index=0
    for j in range(0,len(b)):
        n=0
        for k in range(j+1,len(b)):
            if b[j]==b[k]:
                n=k-j-1
                index=1
            if n>nums:
                nums=n
            n=0
    if index!=0:
        print(nums)
    else:
        print(-1)