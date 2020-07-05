a=eval(input())
for i in range(a):
    c=input()
    b=[int(x) for x in input().split()]
    c=int(c)
    d={}
    for j in b:
        temp=b.count(j)
        d[j]=temp
    count=0
    for j in d.keys():
        count+=(d[j]-1)*d[j]/2
    print(int(count))