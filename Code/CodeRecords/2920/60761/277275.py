n,k=map(int,input().split())
list1=list(map(int,input().split(" ")))
temp=[]
for i in range(len(list1)-1):
    temp.append(list1[i+1]-list1[i])
temp.sort()
print(sum(temp[:len(temp)-k+1]))
