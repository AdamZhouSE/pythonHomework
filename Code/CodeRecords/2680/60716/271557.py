def fuc(n):
    if n == 0: return 1
    elif n >= 1: return n * fuc(n - 1)
    else: print('出错')
ucnum = int(input())
ans = list()
for i in range(ucnum):
    m,n = map(int,input().split())
    a = fuc(m+n-2)
    b = fuc(m-1)
    c = fuc(n-1)
    ans.append(a//(b*c))
for i in ans:
    print(i)