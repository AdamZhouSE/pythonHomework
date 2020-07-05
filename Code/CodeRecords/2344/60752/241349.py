num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    d=int(input())
    eles2=eles[d:]
    eles2.extend(eles[0:d])
    print(' '.join(list(map(str,eles2)))+' ')