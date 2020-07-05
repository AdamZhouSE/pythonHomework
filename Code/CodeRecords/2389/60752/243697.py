num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    eles.sort()
    a=0
    while a<int(size/2)*2:
        save=eles[a]
        eles[a]=eles[a+1]
        eles[a+1]=save
        a+=2
    print(' '.join(map(str,eles)))


