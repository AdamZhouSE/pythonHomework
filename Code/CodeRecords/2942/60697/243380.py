size=int(input())
nums=list(map(str,input().split(' ')))
nums.sort(reverse=True)
for i in nums:
    print(i,end="")