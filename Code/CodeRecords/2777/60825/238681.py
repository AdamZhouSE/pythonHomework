N=int(input())
for i in range(N):
    length=int(input())
    a=input()
    l=a.split()
    l= list(map(int, l))
    l.sort()
    if length%2==1:
        print(l[int((length+1)/2)-1])
    else:
        print(int( (l[int(length/2)-1]+l[int(length/2)])/2 ))