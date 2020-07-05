row = input()
column = input()
ops = int(input())
op = []
for i in range(ops):
    op.append(input().split(","))
minr = row
minc = column
for i in range(len(op)):
    if op[i][0] < minr:
        minr = op[i][0]
    if op[i][1] < minc:
        minc = op[i][1]
nums = int(minr) * int(minc)
print(nums)