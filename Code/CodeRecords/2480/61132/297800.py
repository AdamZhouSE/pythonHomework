n = int(input())
for j in range(n):
    n = int(input())
    l=list(input())
    ou=[i for i in l if i%2==0]
    ji=[i for i in l if i%2==1]
    l=ou+ji
    print(' '.join(l))