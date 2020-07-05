import re
t = int(input())
for i in range(t):
    n = int(input())
    inp = input()
    arr =[int(x) for x in re.split(", | ",inp.strip())]
    hash = {}
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            sum = arr[i]+arr[j]
            if sum in hash:
                a,b=hash[sum]
                ans.append((a,b,i,j))
            else:
                hash[sum]=(i,j)
    if ans==[]:
        print("no pairs")
    else:
        ans.sort()
        print(*ans[0])