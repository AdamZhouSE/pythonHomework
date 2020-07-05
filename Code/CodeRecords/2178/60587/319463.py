n=int(input())
num=[int(n) for n in input().split()]
for i in range(1,len(num)+1):
    a=[]
    for j in range(i):
        a.append(num[j])
    ss=[]
    for x in range(1,len(a)+1):
        for y in range(len(a)+1-x):
            tt=[]
            for z in range(y,y+x):
                tt.append(a[z])
            if tt not in ss:
                ss.append(tt)
    print(len(ss))