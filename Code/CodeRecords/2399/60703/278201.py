T = int(input())
def fac(n:int):
    t = 1
    for i in range(1,n+1):
        t*=i
    return t
for i in range(T):
    in1 = [int(x) for x in input().split()]
    n, m, l, r = in1[0],in1[1],in1[2],in1[3]
    nums = [int(x) for x in  input().split()]

    lenChoose  = r-l+1
    dic = dict()
    for j in nums:
        if j not in dic:
            dic[j] = 1
        else:
            dic[j]+=1

    times = (m//lenChoose)
    remainder = m%lenChoose
    # for j in range(l,r+1):
    #     if j not in dic:
    #         dic[j] = times
    #     else:
    #         dic[j]+= times
    for t in range(l,r+1):
        if t not in dic:
            dic[t] = 0
    for t in range(m):
        sortedDic = sorted(dic.items(),key = lambda x:x[1])
        for item in sortedDic:
            if item[0]<=r and item[0]>=l:
                dic[item[0]]+=1
                break
    fa = fac(m+n)
    for key in dic:
        temp = fac(dic[key])
        fa = fa//temp

    res = fa%998244353
    print(fa%998244353)
    # if(res == 3780):
    #     print(in1)
    #     print(nums)
    #     break


    
