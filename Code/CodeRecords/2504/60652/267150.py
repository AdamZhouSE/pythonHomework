arr=list(map(int,input().replace('[','').replace(']','').split(',')))
index=0
points=[]
while index<len(arr):
    points.append([arr[index],arr[index+1]])
    index+=2
f=lambda x: x[0]**2+x[1]**2
points.sort(key=f)
K=int(input())
print(points[:K])