def kClosest(points, K):
    points.sort(key = lambda P: P[0]**2 + P[1]**2)
    return points[:K]
str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
i=0
points=[]
while i<len(list1):
    list2=[]
    list2.append(int(list1[i]))
    list2.append(int(list1[i+1]))
    points.append(list2)
    i=i+2
k=int(input())
ans=kClosest(points,k)
print(ans)