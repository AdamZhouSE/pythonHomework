a=input().split(",")
l=[]
for i in range(len(a)):
    l.append(int(a[i]))
l.sort(reverse=True)

k=int(input())
print(l[k-1])
             