arr = list(map(int, input().split()))
k, m, ops = arr[0], arr[1], []
word, n = input(), eval(input())
for i in range(0, n):
    ops.append(list(map(int, input().split())))
for op in ops:
    a, b, c = op[0], op[1], op[2]
    t = word[a:b]
    word = word[0:c] + t + word[c:]
    if len(word) > m:
        word = word[0:m]
print(word[0:k], end='')