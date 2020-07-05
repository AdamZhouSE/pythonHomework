n=int(input())
max=0
num=list(input().split(" "))
level=list(input().split(" "))
for i in range(int(level[0])-1,int(level[1])-1):
    max=max+int(num[i])
print(max)