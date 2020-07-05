t=int(input())
for i in range(0,t):
    n=int(input())
    a=[int(k) for k in input().split()]
    setlist=list(set(a))
    numlist=[[0]*2]*len(setlist)
    for i in range(0,len(setlist)):
        numlist[i][0]=setlist[i]
        numlist[i][1]=a.count(setlist[i])
    for i in range(1,len(setlist)):
        for j in range(0,len(setlist)-i):
            if numlist[j][1]<numlist[j+1][1]:
                numlist[j],numlist[j+1]=numlist[j+1],numlist[j]
    string=''
    for i in range(0,len(setlist)):
        string=string+numlist[i][1]*str(numlist[i][0])+' '
    print(string[:len(string)-1])