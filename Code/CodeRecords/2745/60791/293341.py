begin = input()
end = input()
l = eval(input())
pro = []
for i in range(len(end)+1):
    pro.append([])

for i in range(len(l)):
    index = 0
    for j in range(len(l[i])):
        if l[i][j] == end[j]:
            index += 1
    pro[index].append(l[i])
print([])