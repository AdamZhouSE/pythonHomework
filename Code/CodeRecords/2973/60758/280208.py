str1=[i for i in input()]
n=int(input())
visited=[]
count=0
for j in range(0,n):
    str2=[i for i in input()]
    str2.sort()
    len2=len(str2)
    for i in range(0,len(str1)-len2+1):
        list2=str1[i:i+len2]
        list1=str1[i:i+len2]
        list1.sort()
        if(list1==str2 and (list2 not in visited) ):
            visited.append(list2)
            count+=1
print(count)