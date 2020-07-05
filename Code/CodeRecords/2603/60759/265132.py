lst = eval(input())
n = int(input())
diff = []
for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
        diff.append(abs(lst[j] - lst[i]))
diff.sort()
print(diff[n - 1])
