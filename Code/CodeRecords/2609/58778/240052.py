n=int(input())
for i in range(n):
    s=input()
    st=input()
    sl1=s.split( )
    stl=st.split( )
    numlist=[]
    for x in stl:
        numlist.append(int(x))
    countlist=[]
    for x in numlist:
        if(numlist.count(x)==1):
            countlist.append(x)
    k=int(sl1[1])
    if(k>len(countlist)):
        print(-1)
    else:
        print(countlist[k-1])