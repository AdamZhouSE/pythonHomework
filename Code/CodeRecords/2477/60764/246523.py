T=int(input())
for t in range(T):
    s1=list(map(int,input().split()))
    s2=list(map(int,input().split()))
    point=[[s2[0],s2[1]],[s2[0],s2[3]],[s2[2],s2[1]],[s2[2],s2[3]]]
    res=0
    for i in range(4):
        if point[i][0]>min(s1[0],s1[2]) and point[i][0]<max(s1[0],s1[2]):
            if point[i][1]>min(s1[1],s1[3]) and point[i][1]<max(s1[1],s1[3]):
                res=1
                break
    print(res)