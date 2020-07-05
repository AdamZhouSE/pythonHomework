def cutting_trees(x,h,n):
    res=2
    for i in range(1,n-1):
        # 最左边的可以往左倒，最有边的可以往右倒
        left_cut=right_cut=False
        if x[i]-h[i]>x[i-1]:left_cut=True
        if x[i]+h[i]<x[i+1]:right_cut=True
        if left_cut:
            res += 1
        elif right_cut:
            x[i]=x[i]+h[i]
            res+=1
    return res

n=int(input())
x,h=[],[]
for _ in range(n):
    inp=input().split()
    x.append(int(inp[0]))
    h.append(int(inp[1]))
print(cutting_trees(x,h,n))