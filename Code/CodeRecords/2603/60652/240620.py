s=input().replace('[','').replace(']','')
l=list(map(int,s.split(',')))
k=int(input())
n=len(l)
distance=[]
for i in range(0,n-1):
    for j in range (i+1,n):
        distance.append(abs(l[i]-l[j]))
distance.sort()
print(distance[k-1])