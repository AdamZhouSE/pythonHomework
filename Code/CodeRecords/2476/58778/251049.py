n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    sl=s.split( )
    numlist=[]
    for j in sl:
        numlist.append(int(j))
    numlist.sort()
    sum=0
    while len(numlist)>=2:
        sum=sum+numlist[0]+numlist[1]
        t=numlist[0]+numlist[1]
        del numlist[0]
        del numlist[0]
        numlist.append(t)
        numlist.sort()
    print(sum)