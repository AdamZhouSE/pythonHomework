val = [eval(input()) for _ in range(eval(input()))]
count = 0
for i in range(1, len(val)):
    min_val = min([abs(val[j] - val[i]) for j in range(i)])
    count += min_val
print(count + val[0], end='')