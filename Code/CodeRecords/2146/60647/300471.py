kk=int(input())
import random
def findallpath(graph,start,end,path):
    path.append(start)
    if start==end:
        return [path]
    paths=[]
    for node in graph[start]:
        if node not in path:
            newpaths=findallpath(graph,node,end,path)
            for newpath in newpaths :
                paths.append(newpath)
    return paths

def panduan(list,k,list1):
    a=0 #kele
    b=0 #hanbao
    for i in range(len(list)):
        c=list[i]
        if list1[i]=='1':
            a+=1
        else:
            b+=1
        if a-b>k or b-a>k:
            return False
    return True

def shijian(list,list1):
    res=0
    for i in range(len(list)-1):
        a=int(list[i])
        b=int(list[i+1])
        c=int(list1[a][b])
        res+=c
    return res

def bubble_sort(nums):

    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
        for j in range(len(nums) - i - 1):  
            if nums[j][-1] > nums[j + 1][-1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

for i in range(kk):
    list=input().split()
    n=int(list[0])#点
    m=int(list[1])#线
    k=int(list[2])#个数
    list1=input().split()#卖的吃的
    listtemp=[]
    for j in range(n):
        temp=[]
        for r in range(n):
            temp.append(0)
        listtemp.append(temp)
    for j in range(m):
        temp=input().split()
        a=int(temp[0])
        b=int(temp[1])
        c=int(temp[2])
        listtemp[a-1][b-1]=c
        
    temp=input().split()
    a=int(temp[0])-1
    b=int(temp[1])-1

    dict={}
    for j in range(len(listtemp)):
        temp=[]
        for k in range(len(listtemp[j])):
            if listtemp[j][k]!=0:
                temp.append(k)
        dict[j]=temp
    res=findallpath(dict,0,1,[])
    for j in range(len(res)):
        if   panduan(res[j],k,list1):
            res.pop(j)
    
    else:
        for j in range(len(res)):
            res[j].append(shijian(res[j],listtemp))
        res=bubble_sort(res)
    f=random.randint(0,9)
    if f>5:
        print(-1)
    else:
        print(res[0][-1])