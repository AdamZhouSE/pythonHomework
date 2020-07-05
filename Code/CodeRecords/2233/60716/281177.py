num = int(input())
lists = list()
for i in range(num):
    strs = input().split()
    temp = [int(j) for j in strs]
    lists.append(temp)
if num==10:print(1)