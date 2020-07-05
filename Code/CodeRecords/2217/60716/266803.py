lists = list()
for i in range(4):
    strs = input().split(',')
    temp = [int(k) for k in strs]
    lists.append(temp)
a,b,c,d = lists
print(a)