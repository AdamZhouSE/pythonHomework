test=int(input())
for i in range(test):
    s=input()
    only=set(s)

    count=[]
    for i in range(len(s)):
        for k in range(len(s),0,-1):
            sub=s[i:k]
            onlySub=set(sub)
            if onlySub==only:
                count.append(len(sub))
    print(min(count))