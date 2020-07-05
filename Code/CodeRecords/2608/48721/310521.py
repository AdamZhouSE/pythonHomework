n=int(input())
for i in range(n):
    s=""
    s=input()
    l=list(s)
    l.sort()
    if "a" in l:
        res="a"
        for m in range(1,len(l)):
            a=l[m]
            res=res+a
            
            print(res)
    else:
        print(-1)