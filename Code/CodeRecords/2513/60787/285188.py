n=int(input())
m=[]
for i in range(0,n):
    temp=[int(i) for i in input().split(",")]
    m.append(temp)
k=int(input())
re=[m[0][0]]
for i in range(0,n):
    for j in range(0,n):
        if not(i==0 and j==0):
            for t in range(0,len(re)):
                if re[t]>m[i][j]:
                    re.insert(t,m[i][j])
                    break
            else:
                re.append(m[i][j])
print(re[k-1])