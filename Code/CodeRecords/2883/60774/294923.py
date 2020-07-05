s = input().split(' ')
m = int(s[0])
n = int(s[1])
matrix = []
for i in range(0,m):
    matrix.append(input())
for j in range(0,m):
    det = matrix[j].count('B')
    if(det >= 1):
        result = [j + 1 + int(det / 2),matrix[j].find('B') + 1 +int(det / 2)]
        break
print(str(result[0]) + ' ' + str(result[1]))        