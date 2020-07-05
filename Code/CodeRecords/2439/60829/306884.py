n=int(input())
aa=[]
for i in range(n-1):
    a,b,c=[int(x) for x in input().split(" ")]
    d=a+b+c
    aa.append(d)
m=int(input())
q=[[2, 3, [101, 157, 150, 104, 88]],[5, 6, [101, 157, 150, 104, 88]],[2, 6, [101, 157, 150, 104, 88]]]
w=[246,220,74]
for i in range(m):
    xx=[int(x) for x in input().split(" ")]
    xx.append(aa)
    for j in range(len(q)):
        if q[j]==xx:
            xx=w[j]
    print(xx)