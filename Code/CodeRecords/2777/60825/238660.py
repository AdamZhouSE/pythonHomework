N=int(input())
for i in range(N):
    length=int(input())
    a=input()
    l=a.split("")
    l= list(map(int, l))
    l.sort()
    if length%2==1:
        print(l[(length+1)/2-1])
    else:
        print(23423)