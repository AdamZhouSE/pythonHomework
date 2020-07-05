nums = int(input())
list1 = []
list2 = []
for m in range(nums * 3):
    list2.append(input())
for i in range(len(list2)):
    if not list2[i][-1].isdigit():
        list2[i] = list2[i][:-1]
    list2[i] = list2[i].split(" ")
    for j in range(len(list2[i])):
        list2[i][j] = int(list2[i][j])
k = 0
while k < nums * 3:
    n_x_y = list2[k]
    A = list2[k + 1]
    B = list2[k + 2]
    n = int(n_x_y[0])
    x = int(n_x_y[1])
    y = int(n_x_y[2])
    i, j = len(A) - 1, len(B) - 1
    count_a, count_b, max_sum = 0, 0, 0
    while i >= 0:
        if int(A[i]) >= int(B[j]):
            count_a += 1
            max_sum += int(A[i])
            i -= 1
            j -= 1
        else:
            count_b += 1
            max_sum += int(B[j])
            i -= 1
            j -= 1
    list1.append(max_sum)
    k += 3
for i in list1:
    print(i)