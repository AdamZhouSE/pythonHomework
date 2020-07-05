num = int(input())
lists = []
for i in range(num):
    a,b,c,d = map(int,input().split())
    lists.append(a+b+c+d)
index = 1
for i in range(num):
    if lists[0]<lists[i]:
        index+=1
print(index)