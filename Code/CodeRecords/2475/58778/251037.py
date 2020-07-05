n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    sl=s.split( )
    temp=[]
    for j in sl:
        temp.append(int(j))
    temp.sort()
    cout=[]
    for j in range(len(temp)-1):
        c=0
        for k in range(j+1,len(temp)):
            if(temp[k]!=temp[k-1]+1):
                c=c+1
                break
            else:
                c=c+1
        cout.append(c)
    #print(temp)
    #print(cout)
    print(max(cout))