def research(list2):
    flag=1
    while len(list2)!=1:
        list3=[]
        for i in range(0,int(len(list2)/2)):
            if flag==1:
                list3.append(list2[2*i]|list2[2*i+1])
            else:
                list3.append(list2[2*i]^list2[2*i+1])
        list2=list3
        flag^=1
    print(list2[0])
                
tmp=input().split()
n=int(tmp[0])
m=int(tmp[1])
list1=input().split()
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
for i in range(0,m):
    tmp=input().split()
    p=int(tmp[0])
    b=int(tmp[1])
    list1[p-1]=b
    list2=list1.copy()
    research(list2)