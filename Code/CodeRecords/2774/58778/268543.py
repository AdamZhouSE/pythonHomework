n=int(input())
for i in range(n):
    s=input()
    sl=s.split( )
    k=int(sl[1])
    m=input()
    numlist=[]
    for j in m.split( ):
        numlist.append(int(j))
    numlist.sort()
    i=1
    while(sum(numlist[:i])<k and i!=len(numlist)+1):
        i=i+1
    print(i-1)