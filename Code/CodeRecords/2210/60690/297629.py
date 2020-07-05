t=int(input())
res=[]
for i in range(t):
    s1=input()
    s2=input()
    this=""

    for l in range(len(s1)-len(s2)+1):
        for r in range(l+len(s2),len(s1)):
            str=s1[l:r+1]
            isIn=True
            for e in s2:
                if e not in str:
                    isIn=False
                    break
            if isIn:
                if this=="":
                    this=str
                else:
                    if len(this)>len(str):
                        this=str
    if this=="":res.append(-1)
    else:res.append(this)
for e in res:
    print(e)
