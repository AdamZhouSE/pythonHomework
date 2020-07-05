s = input()
matrix = []
while(True):
    s = input().strip().strip(',')
    if(s == ']'):
        break
    s = list(map(int,s[2:-2].split('","')))
    matrix.append(s)
print(matrix)