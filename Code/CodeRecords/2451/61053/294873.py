lst = input().split(',')
numlst = eval(lst[0])
k = int(lst[1])
index = 0
while index < len(numlst):
    if numlst[index] < k:
        index += 1
print(index)