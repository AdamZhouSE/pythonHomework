n=int(input())
for k in range(n):
    tl=int(input())
    lst=[]
    list0=input().split()
    if list0[0][-1]==',':
        for i in range(len(list0)-1):
             list0[i]=list0[i][0:-1]
    list0=[int(x) for x in list0]
    for i in range(len(list0)):
        for j in range(i+1,len(list0)):
            list1=[list0[i]+list0[j],i,j]
            lst.append(list1)
    # print(lst)
    isF=False
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)-1):
            if lst[i][0]==lst[j][0]:
                isF=True
                print(lst[i][1],lst[i][2],lst[j][1],lst[j][2])
                break
        if isF:
            break
    if not isF:
        print('no pairs')

