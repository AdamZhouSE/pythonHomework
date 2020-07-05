a=int(input())
b=[int(i) for i in input().split()]
jishu=[]
oushu=[]
for i in range(0,a):
    if b[i]%2==0:
        oushu.append(b[i])
    else:
        jishu.append(b[i])
jishu.sort()
oushu.sort()
if len(jishu)==len(oushu) or abs(len(jishu)-len(oushu))==1:
    print(0)
else:
    if len(jishu)>len(oushu):
        index=len(jishu)-len(oushu)-1
        sums=0
        for j in range(0,index):
            sums=sums+jishu[j]
        print(sums)
    else:
        index=len(oushu)-len(jishu)-1
        sums=0
        for j in range(0,index):
            sums=sums+oushu[j]
        print(sums)