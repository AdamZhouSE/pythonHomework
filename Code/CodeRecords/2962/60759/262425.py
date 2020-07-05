def increment(num, k, length):
    while k > 0:
        num = (num + 1) % length
        k -= 1
    return num


n, p = eval(input().replace(' ', ','))
str_lst = input().split(' ')
hash_lst = ['' for i in range(p)]
ans = ''
for i in range(n):
    end = str_lst[i][len(str_lst[i]) - 3:]
    pos = 0
    for j in range(3):
        pos += (ord(end[j]) - ord('A')) * 32 ** (2 - j)
    offset = [1, 6]
    idx = 0
    pos %= p
    while hash_lst[pos] != '':
        pos = increment(pos, offset[idx], p)
        idx += 1
    hash_lst[pos] = str_lst[i]
    ans += str(pos) + ' '
print(ans.rstrip())
