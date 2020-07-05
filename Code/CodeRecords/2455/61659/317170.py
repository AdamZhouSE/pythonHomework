n=int(input())
nums=input().split(' ')
nums=[int(x) for x in nums]
link=[]
for i in range(n-1):
    link.append([int(x) for x in input().split(' ')])
