inp = input().split(" ")
n = int(inp[0])  #孩子数量
k = int(inp[1])  #体重分界点
child = input().split(" ") #孩子的体重
count = 0
for i in range(n):
    if(int(i)<=k):
        count = count +1
        
print(count)
