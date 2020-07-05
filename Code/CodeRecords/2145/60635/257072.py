tests = int(input())
for t in range(tests):
    n=int(input())
    heights=[int(x) for x in input().split()]
    ans=[]
    for i in range(n):
        for j in range(i+1,n+1):
            ans.append(min(heights[i:j])*(j-i))
    print(max(ans))
    