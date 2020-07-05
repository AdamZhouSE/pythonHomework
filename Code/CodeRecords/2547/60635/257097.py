tests = int(input())
for t in range(tests):
    n=int(input())
    array=[int(x) for x in input().split()]
    k = int(input())
    repo=[]
    ans=[]
    for a in array:
        tmp1=a+k
        tmp2=a-k
        tmp=[]
        if tmp1 in repo:
            tmp.append(tmp1)
        if tmp2 in repo:
            tmp.append(tmp2)
        for t in tmp:
            tup =(min(t,a),max(t,a))
            if tup not in ans:
                ans.append(tup)
        repo.append(a)
    print(len(ans))