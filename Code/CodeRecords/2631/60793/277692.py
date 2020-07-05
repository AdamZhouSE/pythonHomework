#def max_num_count(ls0: list) -> int:
ls = []
temp0 = list(map(int, input().split()))
n, g = temp0[0], temp0[-1]
for i in range(0, n):
    ls.append(list(map(int, input().split())))
ls = sorted(ls, key=lambda x: x[0])
temp1 = sorted(ls, key=lambda x: x[1], reverse=True)
cows = [0 for x in range(0, temp1[0][1])]
count = 0
log = []
print(ls)
if ls[0][2] < 0:
    print("???")
ls = [x[1] - 1 for x in ls]
print(ls)


