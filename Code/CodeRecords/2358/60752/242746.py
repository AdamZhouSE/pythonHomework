num=int(input())
for i in range(num):
    line1=list(map(int,input().split(' ')))
    size=line1[0]
    k=line1[1]
    a=list(map(int,input().split(' ')))
    a.sort(reverse=True)
    print(' '.join(map(str,a[0:k]))+' ')
 
