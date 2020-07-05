def time_separate(arr,num,temp,lis):
    if min(lis)==1:
        print(num)
        return
    for i in range(0,len(arr)):
        if lis[i]==1:
            continue
        elif arr[i][0]>=temp:
            temp=arr[i][1]
            lis[i]=1
    if min(lis)==1:
        print(num)
        return
    else:
        time_separate(arr,num+1,0,lis)

def takeSecond(elem):
    return elem[1]

num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    arr=[]
    for j in range(n):
        arr.append([list1[j],list2[j]])
    arr.sort(key=takeSecond)
    lis=[0 for x in range(n)]
    time_separate(arr,1,0,lis)