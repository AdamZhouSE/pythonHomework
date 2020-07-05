num = int(input())
for x in range(0,num):
    list1=list(map(int, input().split(" ")))
    list2=list(map(int, input().split(" ")))
    unread=[1]*(list1[0]+1)
    read=[0]*(list1[0]+1)
    trash=[0]*(list1[0]+1)
    for i in range(0,len(list2)):
        if i%2==0:
            if list2[i]==1:
                unread[list2[i+1]]=0
                read[list2[i+1]]=1
            elif list2[i]==2:
                read[list2[i+1]]=0
                trash[list2[i+1]]=1
            elif list2[i]==3:
                unread[list2[i+1]]=0
                trash[list2[i+1]]=1
            elif list2[i]==4:
                trash[list2[i+1]]=0
                read[list2[i+1]]=1
    a=False
    b=False
    c=False
    for j in range(1,list1[0]+1):
        if unread[j]!=0:
            a=True
            print(j,end=" ")
    if not a:
        print("EMPTY")
    print()
    for j in range(1,list1[0]+1):
        if read[j]!=0:
            b=True
            print(j,end=" ")
    if not b:
        print("EMPTY")
    print()
    for j in range(1,list1[0]+1):
        if trash[j]!=0:
            c=True
            print(j,end=" ")
    if not c:
        print("EMPTY")
    print()