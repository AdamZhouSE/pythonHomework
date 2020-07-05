num_list =list(map(int,input().split(" ")))
n=num_list[1]
length=num_list[0]
res=input().split(" ")
k=res.count('')
for j in range(0,k):
    res.remove('')
res=list(map(int,res))
for i in range(0,n):
    num_list=input().split(" ")
    k=num_list.count('')
    for j in range(0,k):
        num_list.remove('')
    num_list=list(map(int,num_list))
    if(num_list[0]!=3):
        l=num_list[1]
        r=num_list[2]
    if(num_list[0]==1):
        temp=res[l-1:r]
        temp.sort()
        print(temp.index(num_list[3])+1)
    elif(num_list[0]==2):
        temp = res[l - 1:r]
        temp.sort()
        print(temp[num_list[3]-1])
    elif(num_list[0]==3):
        res[num_list[1]-1]=num_list[2]
    elif(num_list[0]==4):
        temp = res[l - 1:r]
        temp.sort()
        for i in range(len(temp)-1,-1,-1):
            if temp[i]<num_list[3]:
                print(temp[i])
                break
    elif(num_list[0]==5):
        temp = res[l - 1:r]
        temp.sort()
        for i in range(0, len(temp)):
            if temp[i] > num_list[3]:
                print(temp[i])
                break