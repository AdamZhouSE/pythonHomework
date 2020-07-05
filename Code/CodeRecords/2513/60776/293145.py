a=int(input())
list=[]
for i in range(0,a):
    b=input().split(',')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    list.extend(b)
list.sort()
k=int(input())
print(list[k-1])