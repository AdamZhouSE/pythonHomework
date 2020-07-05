tree=[]
time=int(input())
while(time>0):
    time-=1
    str0=input()
    list0=str0.split()
    
    op=int(list0[0])
    string=list0[1]
    
    if(op==1):
        tree.append(string)
    elif(op==2):
        index=0
        for i in range(len(tree)):
            if(tree[i]==string):
                index=i
                break
        del tree[index]
    elif(op==3):
        have=False
        for s in tree:
            if(s==string):
                have=True
                break
        if(have):
            print("YES")
        else:
            print("NO")
    elif(op==4):
        length=len(string)
        count=0
        for s in tree:
            if(s[:length]==string):
                count+=1
        print(count)