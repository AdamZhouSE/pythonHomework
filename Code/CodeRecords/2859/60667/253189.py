num = int(input())
edges = []
for i in range(num):
    edges.append(input())

for i in range(num):
    check = ''
    if edges[i][i] != edges[i][num - i - 1]:
        print('NO')
        quit()
    if i < (num-1)/2:
        left = edges[i][:i] + edges[i][i + 1:num - i - 1] + edges[i][num - i:]
    elif i ==(num-1)/2:
        left = edges[i][:i]+edges[i][i+1:]
    else:
        left = edges[i][:num-i-1] + edges[i][num - i :i] + edges[i][i+1:]
    for j in left:
        if j not in check:
            check = check + j
    if len(check) != 1:
        print('NO')
        quit()

    if check == edges[i][i]:
        print('NO')
        quit()
        
print('YES')