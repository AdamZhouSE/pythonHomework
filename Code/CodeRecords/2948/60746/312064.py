initial=list(input())
ST=int(input())
def ToNum(N,S):
    n=len(N)
    new=[]
    for i in range(0,n-1):
        a=int(S+ord(N[i])-65)
        a1=int(a%10)
        a2=int(((a-a1)/10)%10)
        a3=int(((((a-a1)/10)-a2)/10)%10)
        a4=int(((((((a-a1)/10)-a2)/10)-a3)/10)%10)
        if a4!=0:
            new.append(a4)
        new.append(a3)
        new.append(a2)
        new.append(a1)
    return new
def fate(N,S):
    new=ToNum(N,S)
    nn=len(new)
    t=nn+1
    for i in range(nn-2):
        t=t-1
#        print('t=',t)
        for j in range(t-1):
            new[j]=(new[j]+new[j+1])%10
#            print(new[j])
        a=new[0]*100+new[1]*10+new[2]
#        print('a=',a)
        if a<=100 and new[2]!=0:
            break
        elif a==100:
            break
        elif a<100 and new[2]==0:
            a=int(a/10)
    return a

'''
        if new[0]==0 and t<=4:
            break
        elif new[0]==1 and new[1]==0 and new[2]==0:
            break
    if t>3:
        return (new[0]*100+new[1]*10+new[2])
    else:
        return (new[0]*10+new[1])
'''
    
#print(ToNum(initial,ST))
print(fate(initial,ST))