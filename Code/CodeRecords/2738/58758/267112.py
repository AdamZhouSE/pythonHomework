inp = input()
mat = []
while True:
    inp = input()
    if inp[len(inp)-1] == ',':
        nums = eval(inp[2: len(inp)-1])
        mat.append(nums)
    elif inp == ']':
        break
    else:
        nums = eval(inp[2: len(inp)])
        mat.append(nums)
length = len(mat)
width = len(mat[0])


def isvalid(i, j, row, column):
    for m in range(i, i+row):
        for n in range(j, j+column):
            if mat[m][n] != '1':
                return False
    return True


ans = 0
for row in range(1, length):
    for column in range(1, width):
        for i in range(0, length-row+1):
            for j in range(0, width-column+1):
                if isvalid(i, j, row, column) and column * row > ans:
                    ans = column * row
print(ans)
