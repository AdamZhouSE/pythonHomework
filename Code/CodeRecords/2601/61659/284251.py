m=int(input())
n=int(input())
k=int(input())
lists=[m*n]*k

for i in range(1,m+1):
    for j in range(1,m+1):
        if i*j<max(lists):
            lists[lists.index(max(lists))]=i*j

print(max((lists)))
