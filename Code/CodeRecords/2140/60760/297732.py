tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(int(input()))
print(lists)
for i in lists:
    print(func(i))