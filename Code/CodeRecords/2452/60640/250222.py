line = int(input())
matrix = []
for i in range(line):
    inp = list(map(int, input().split(",")))
    matrix.append(inp)
target = int(input())
hit = False
for i in range(line):
    if matrix[i][-1] >= target:
        for num in matrix[i]:
            if num == target:
                hit = True
                break
print(hit)
