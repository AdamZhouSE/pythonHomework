sum = eval(input())
lst = []
for i in range(sum):
    lst.append(eval(input()))
max = 0.0;
for i in range(sum - 2):
    for j in range(i + 1, sum - 1):
        for k in range(j + 1, sum):
            s = float((lst[i][0] * (lst[j][1] - lst[k][1]) + lst[j][0] * (lst[k][1] - lst[i][1]) + lst[k][0] * (lst[i][1] - lst[j][1])))
            if s > max:
                max = s
print(max)
