num = int(input())
m = [None] * num
for i in range(num):
    m[i] = input()
    m[i] = ''.join(sorted(list(m[i])))
m = list(set(m))
print(len(m),end='')
