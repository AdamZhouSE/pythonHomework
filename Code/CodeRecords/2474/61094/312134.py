n = int(input())
while(n>0):
    m = input()
    l = len(m)
    value = 0
    num = 0
    for i in range(0,l):
        if m[i]=='(':
            if value<0:
                value = 0
            value+=1
        else:
            if value>0:
                num+=1
            value-=1
    print(2*num)
    n-=1