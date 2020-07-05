lst = input().split(',')
lst[0] = lst[0][1:]
lst[len(lst)-1] = lst[len(lst)-1][:-1]
lst = list(map(int,lst))

#前i项和
formerSum = []
for i in range(len(lst)):
    formerSum.append(sum(lst[0:i+1]))
print(max(formerSum)-min(formerSum))