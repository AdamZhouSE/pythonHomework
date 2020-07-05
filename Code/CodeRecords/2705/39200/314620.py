pairs = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("], [")]
n = len(pairs)
M = [[0 for y in range(n)]for x in range(n)]
#print(pairs)
value = 0
for i in pairs:
    M[i[0] - 1][i[1] - 1] = 1
for y in range(n):
    hasparent = 0
    issingleparent = 1
    for x in range(n):
        if M[x][y] == 1:
            if hasparent == 0:
                hasparent = 1
            else:
                issingleparent = 0
                break
    if issingleparent == 0:
        value = y + 1
i = []
for i in pairs[::-1]:
    if i[1] == value:
        break
print(i)
    
#print(M)
#  1 2 3
#1 \ 1 1
#2 0 \ 1
#3 0 0\