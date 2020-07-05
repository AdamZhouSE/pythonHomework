A = eval(input())
re = []
rest = len(A)


def move(n):
    temp = []
    for i in range(n):
        temp.append(A[i])
    temp.reverse()
    for i in range(n):
        A[i] = temp[i]


while rest > 1:
    max_num = A[0]
    max_index = 0
    for i in range(rest):
        if A[i] > max_num:
            max_num = A[i]
            max_index = i
    if max_index != 0:
        re.append(max_index + 1)
        move(max_index + 1)
    re.append(rest)
    move(rest)
    rest -= 1
print(re)