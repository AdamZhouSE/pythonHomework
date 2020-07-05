a_b = input().split()
a = a_b[0]
b = a_b[1]
a_list = []
b_list = []
for i in range(len(a)):
    a_list.append(ord(a[i]))
for i in range(len(b)):
    b_list.append(ord(b[i]))
ans = 0
i = 0
while ans == 0 and i < len(a) and i < len(b):
    ans = a_list[i] - b_list[i]
    i += 1
    if ans != 0:
        break
print(ans)