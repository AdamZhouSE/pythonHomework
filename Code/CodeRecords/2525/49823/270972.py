def at(l):
    
    length=len(l[0])
    t=[[0,0,0] for _ in range(length)]
    for i in range(length):
        t[i][0]=l[0][i]
        t[i][1]=l[1][i]
        t[i][2]=l[2][i]
    t.sort()
    dp=[0 for i in range(length)]
    r,s,p=0,0,0
    for i in range(length):
        for j in range(p,i):
            if t[i][0]>=t[j][1]:
                if j==p:
                    p+=1
                s=max(s,dp[j])
        dp[i]=s+t[i][2]
        r=max(r,dp[i])
    print(r)
if __name__ == '__main__':
    at([eval(input()) for _ in range(3)])
