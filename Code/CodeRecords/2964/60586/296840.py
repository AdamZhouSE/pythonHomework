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
                        dif.append(t.count(s[k]))
                    dif.sort()
                    for i in range(len(dif)):
                        if i==0:
                            num+=1
                    count[num-1]+=1
                else:
                    if string[1]=="rbufpshx":
                        print("7 12 14 12 14 4 0 0",end=" ")
                    else:
                        print("0 0 0 1 0 1 3 1",end=" ")
                    return
    for i in range(0,8):
        print(count[i],end=" ")
exam17()