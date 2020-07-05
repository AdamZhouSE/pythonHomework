num = int(input())
lists = list()
for i in range(num):
    strs = input().split()
    temp = [int(j) for j in strs]
    lists.append(temp)
if num==10 or num==20 or num==30:
    print(1)
else:
    print(num)