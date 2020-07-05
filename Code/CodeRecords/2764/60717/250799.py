n=int(input())
for i in range(0,n):
    list1=[]
    list1.append(int(input()))
    output=list1[0]
    flag=1
    while flag==1:
        flag=0
        list2=[]
        for i in list1:
            list2.append(int(i/2))
            list2.append(int(i/3))
            list2.append(int(i/4))
        for i in list2:
            if i >=12:
                flag=1
            output+=1
        list1=list2.copy()
    print(output)