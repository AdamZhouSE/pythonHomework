"""
现给定n个闭区间[ai, bi]，1<=i<=
这些区间的并可以表示为一些不相交的闭区间的并
你的任务就是在这些表示方式中找出包含最少区间的方案
你的输出应该按照区间的升序排列
这里如果说两个区间[a, b]和[c, d]是按照升序排列的，那么我们有a<=b<c<=d
"""

def special_sort(arr):
    re=[]
    while(len(arr)>0):
        min_num=min(map(min,arr))
        k=0
        while(k<len(arr)):
            if(arr[k][0]==min_num):
                break
            k+=1
        a=[]
        a.append(arr[k][0])
        a.append(arr[k][1])
        re.append(a)
        del arr[k]
    return re


n=int(input())

slist=[]
for i in range(n):
    slist.append([int(m) for m in str(input()).split(" ")])

arr=special_sort(slist)
result=[]
result.append(arr[0])
del arr[0]
hasadd=False
while(len(arr)>0):
    i=0
    hasadd=False
    min_num=arr[0][0]
    max_num=arr[0][1]
    while(i<len(result)):
        if((min_num>=result[i][0] and min_num<=result[i][1]) or (max_num>=result[i][0] and max_num<=result[i][1])):
            result[i][0]=min(min_num,result[i][0])
            result[i][1]=max(max_num,result[i][1])
            hasadd=True
            break
        else:
            i+=1
    if(not hasadd):
        result.append(arr[0])
    del arr[0]

for i in range(len(result)):
    print(str(result[i][0])+" "+str(result[i][1]))