num=int(input())
max_num=0
for i in range(num):
    temp=input().split()
    max_num=max(max_num,int(temp[0])+int(temp[1]))
print(max_num)