num_test = int(input())
ans = []
for i in range(0, num_test):
    num = int(input())
    str_num = bin(num)[2:]
    count = 0
    for j in range(0, len(str_num)):
        if str_num[j] == '1':
            count += 1
    if count % 2 == 0:
        ans.append('even')
    else:
        ans.append('odd')
for k in ans:
    print(k)
