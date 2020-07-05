A = list(eval(input()))
num = []
for i in range(2 ** len(A)):
    temp = []
    for j in range(len(A)):
        if (i >> j) % 2 == 1:
            temp.append(A[j])
    num.append(temp)
re = 0
for i in range(len(num)):
    if len(num[i]) > 1:
        re += (max(num[i]) - min(num[i]))
print(re)