n=int(input())
record=[]
record.append([])
for i in range(n):
    t=input()
    tl=t.split( )
    v=int(tl[0])
    op=int(tl[1])
    x=int(tl[2])
    temp=record[v].copy()
    if(op==1):
        temp.append(x)
        record.append(temp)
    elif(op==2):
        for j in temp:
            if(j==x):
                del temp[temp.index(j)]
                break
        record.append(temp)
    elif(op==3):
        temp.sort()
        print(temp.index(x)+1)
        record.append(temp)
    elif(op==4):
        temp.sort()
        print(temp[x-1])
        record.append(temp)
    elif(op==5):
        c=0
        temp.sort(reverse=True)
        for j in temp:
            if(j<x):
                print(j)
                c=1
                break
        if(c==0):
            print(1-2**31)
        record.append(temp)
    else:
        c=0
        temp.sort()
        for j in temp:
            if(j>x):
                print(j)
                c=1
                break
        if(c==0):
            print(2**31)
        record.append(temp)
    #print(record)