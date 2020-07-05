def delect(l,str):
    for i in range(len(l)):
        if l[i]==str:
            for j in range(i,len(l)-1,1):
                l[j]=l[j+1]
            l=l[:len(l)-1]
            break
    return l
def get(l,str,num):
    l1=[]
    for i in range(len(l)):
        l1.append(l[i])
    for i in range(len(l1)-num,len(l1),1):
        s=l1[i]+str
        l=delect(l,s)
        '''print(s)
        print("before:", end=" ")
        print(l)'''
        l.append(s)
        '''print("after:", end=" ")
        print(l)'''
    l=delect(l,str)
    '''print(str)
    print("before:",end=" ")
    print(l)'''
    l.append(str)
    '''print("after:",end=" ")
    print(l)'''
    return l
    #print(l)
num=int(input())
#print(get(['121', '21', '1', '1212', '212', '12', '2'],'1',4))
l=input().split(" ")
all=[]
for i in range(len(l)):
    all=get(all,l[i],i)
    #print(all)
    print(len(all))