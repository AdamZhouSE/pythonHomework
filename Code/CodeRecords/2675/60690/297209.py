t=int(input())
res=[]
for i in range(t):
    n=input()
    ini=int(n)
    copy=[]
    for j in range(len(n)):
        copy.append(n[j])
    for j in range(len(copy)):
        if copy[j]=="6":
            copy[j]="9"
    n=""
    for j in range(len(copy)):
        n+=copy[j]
    ch=int(n)
    res.append(ch-ini)
for e in res:
    print(e)