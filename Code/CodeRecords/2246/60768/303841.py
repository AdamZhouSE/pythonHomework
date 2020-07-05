n = list(input())
n.sort()
a = ''.join(n)
index = 10 * (len(n) // 3)
if len(n) % 3 == 0:
    index += 7
elif len(n) % 3 == 2:
    index += 4
for i in range(index, index + 4):
    num = sorted(list(str(int(2 ** i))))
    b = ''.join(num)
    if a == b:
        print(True)
        break
else:
    print(False)