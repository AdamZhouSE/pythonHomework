def exam17():
    n=int(input())
    string=[]
    count=[0 for i in range(8)]
    for i in range(n):
        string.append(input())
    for i in range(n):
        s=string[i]
        for j in range(n):
            if j==i:
                break
            t=string[j]
            num = 0
            if len(s)==len(t):
                for k in range(len(s)):
                    if t.count(s[k])!=s.count(s[k]):
                        num+=1
                count[num-1]+=1
            else:
                dis=len(s)-len(t)
                dif=[]
                if dis>0:
                    for k in range(len(s)):
                        dif[k]=t.count(s[k])
                    dif.sort()
                    for i in range(len(dif)):
                        if i==0:
                            num+=1
                    count[num-1]+=1
                else:
                    for k in range(len(t)):
                        dif[k] = t.count(t[k])
                    dif.sort()
                    for i in range(len(dif)):
                        if i == 0:
                            num += 1
                    count[num - 1] += 1
    for i in range(0,7):
        print(count[i],end=" ")
    print(count[7],end="")
exam17()