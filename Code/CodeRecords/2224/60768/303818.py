n = list(input())
n = [int(i) for i in n]
max_num = n[0]
max_index = 0
for i in range(1, len(n)):
    if n[i] >= max_num:
        max_num = n[i]
        max_index = i
n[0], n[max_index] = n[max_index], n[0]  # swap
n = [str(i) for i in n]
print(''.join(n))