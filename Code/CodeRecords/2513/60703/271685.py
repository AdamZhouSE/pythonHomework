n = int(input())
list = []
for i in range(n):
    temp = [int(x) for x in input().split(",")]
    for j in temp:
        list.append(j)
        
list.sort()
k = int(input())
print(list[k-1])