def tb20():
    n=int(input())
    for i in range(n):
        res=0
        h=int(input())
        s=[int(x) for x in input().split(' ')]
        for j in range(h):
            if(s[j]!=0):
                for k in range(j+1,h):
                    if(s[k]==s[j] and k!=j):
                        s[k],s[j]=0,0
                        res+=2
                        break
        print(res)
    return

tb20()