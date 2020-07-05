n=int(input())
for k in range(n):
    num=int(input())
    list1=[]
    list=input().split()
    for i in list:
        list1.append(i)
    res=[]
    for i in range(len(list)-1):
        r=0
        temp=[]
        temp.append(list[i])
        for j in range(i,len(list)-1):
            if int(list[j])<int(list[j+1]):
                temp.append(list[j+1])
                r=j+1
            else:
                for k in range(i,j):
                    list[k]='10000000000'
                break
        if len(temp)>1:
            res.append(temp)
        if r==len(list)-1:
            break
    if len(res)==0:
        print("没有利润")
    else:
        for i in range(len(res)-1):
            print("(",end="")
            print(list1.index(res[i][0]),end=" ")
            print(list1.index(res[i][len(res[i])-1]),end="")
            print(")",end=" ")
        i=len(res)-1
        print("(", end="")
        print(list1.index(res[i][0]), end=" ")
        print(list1.index(res[i][len(res[i]) - 1]), end="")
        print(")")