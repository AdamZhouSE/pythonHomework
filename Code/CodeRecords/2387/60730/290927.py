length, num = map(int, input().split(" "))
m = list(map(int, input().split(" ")))
for i in range(num):
    temp = list(map(int, input().split(" ")))
    flag, l, r = temp[0], temp[1], temp[2]
    if flag == 0:
        m = m[:l-1] + list(sorted(m[l-1:r], reverse=False)) + m[r:]
    else:
        m = m[:l-1] + list(sorted(m[l-1:r], reverse=True)) + m[r:]
q = int(input())
print(m[q - 1])
