num=int(input())
list=[]
rank=[]

for i in range(num):
    list.append(input().split(" "))

for i in range(num):
    rank.append(int(list[i][0])+int(list[i][1])+int(list[i][2])+int(list[i][3]))

smith=rank[0]
rank.sort(reverse=True)

for i in range(num):
    if rank[i]==smith:
        smith=i+1
        break
print(smith)