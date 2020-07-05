ucnum = int(input())
ans = list()
for i in range(ucnum):
    n,l,r = map(int,input().split())
    print("{} {} {}".format(n,l,r))
    temp = list(bin(n))
    for j in range(r-l+1):
        t = len(temp)-l-j
        if temp[t]=='0':
            temp[t]='1'
        else:
            temp[t]='0'
    strs = ''.join(temp)
    index = int(strs,2)
    ans.append(index)
for i in ans:
    print(i)