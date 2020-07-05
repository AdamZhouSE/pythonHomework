a=int(input())
for i in range(0,a):
    cheshu=int(input())
    b = input().split(' ')
    for j in range(0, len(b)):
        b[j] = int(b[j])
    c = input().split(' ')
    for j in range(0,len(c)):
        c[j]=int(c[j])
    pintai=0
    for j in range(1,len(c)):
        dangqian=1
        for k in range(0,j):
            if c[k]>b[j]:
                dangqian=dangqian+1
        if(dangqian>pintai):
            pintai=dangqian
    print(pintai)