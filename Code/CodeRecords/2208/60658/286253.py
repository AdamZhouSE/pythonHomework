t = int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    stack = []
    ans = []
    for i in range(n):
        while len(stack)>0 and stack[-1]>=li[i]:
            stack.pop()
        if len(stack)==0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(li[i])
    print(*ans,end=" \n")