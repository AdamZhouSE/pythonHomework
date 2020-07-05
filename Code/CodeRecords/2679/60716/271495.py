def caculate(n:int):
    if n<3:
        if n==1:
            return 3
        if n==2:
            return 8
    else:
        return 1+n+n*(n-1)//2+n+n*(n-1)+n*(n-1)*(n-2)//2

ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    temp = caculate(num)
    ans.append(temp)
for i in ans:
    print(i)