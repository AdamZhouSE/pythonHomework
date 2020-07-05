t=int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    co=0
    #print(s)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                #print(s[i],s[j],s[k])
                if int(s[i])+int(s[j])==int(s[k]):
                    co=co+1
                elif int(s[j])+int(s[k])==int(s[i]):
                    co=co+1
                elif int(s[k])+int(s[i])==int(s[j]):
                    co=co+1
    if co!=0:
        print(co)
    else:
        print(-1)