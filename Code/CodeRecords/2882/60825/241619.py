def isU(length,l):
    if length<=2:
        print('YES')
        return
    sit=-1
    for i in range(1,length):
        currsit=0
        if l[i]==l[i-1]:
            currsit=1
        if l[i]<l[i-1]:
            currsit=2
        if currsit<sit:
            print('NO')
            return
        sit=currsit
    print('YES')
            
length=int(input())
a=input()
l=a.split()
l= list(map(int, l))

isU(length,l)