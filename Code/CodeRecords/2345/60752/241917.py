num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    eles.append(0)
    eles.sort()
    a=0
    b=0
    for j in range(size):
        if eles[j+1]-eles[j]>1:
            a=int((eles[j]+eles[j+1])/2)
        if eles[j+1]==eles[j]:
            b=eles[j]
        if a!=0 and b!=0:
            break
    print(b,a)