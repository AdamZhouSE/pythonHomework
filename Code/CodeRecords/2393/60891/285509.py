n = int(input())
list_ans = []
for i in range(n):
    x_y_len = [int(j) for j in input().split()]
    x_len = x_y_len[0]
    y_len = x_y_len[1]
    x = [int(j) for j in input().split()]
    y = [int(j) for j in input().split()]
    x.sort()
    y.sort()
    count = 0
    for j in range(x_len):
        for k in range(y_len):
            if x[j] ** y[k] > y[k] ** x[j]:
                count += 1
    list_ans.append(count)
for i in range(n):
    print(list_ans[i])
