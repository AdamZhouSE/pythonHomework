n=int(input())
output=0
list2=input().split()
for i in range(0,n):
    list2[i]=int(list2[i])
    output+=list2[i]
print(max(list2)*n-output)