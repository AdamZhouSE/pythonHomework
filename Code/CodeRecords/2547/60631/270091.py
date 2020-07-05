t=int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    k=int(input())
    co=0
    li=[]
    for i in range(n):
        for j in range(i+1,n):
            if int(s[i]) > int(s[j]) and [s[i],s[j]] not in li:
                li.append([s[i],s[j]])
            elif int(s[j]) >= int(s[i]) and [s[j],s[i]] not in li:
                li.append([s[j],s[i]])
    for ki in li:
        if int(ki[0])-int(ki[1])==k:
            co=co+1
    print(co)