def grayCode(n) :
        res = []
        for i in range(2 ** n):
            res.append((i >> 1) ^ i)
        return res
n = int(input())
start = int(input())
old_list = grayCode(n)
new_list = []
for i in range(2 ** n):
    if old_list[i] == start:
        for j in range(i, 2 ** n):
            new_list.append(old_list[j])
        for j in range(0, i):
            new_list.append(old_list[j])
print(new_list)
