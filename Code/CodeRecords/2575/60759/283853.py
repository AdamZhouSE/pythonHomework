seq = input()
no = []
queue = []
for ch in seq:
    if ch == '(':
        no.append(len(queue))
        queue.append(ch)
    elif ch == ')':
        queue.pop()
        no.append(len(queue))
temp_s = ' '.join(map(str, no))
for i in range(max(no) // 2 + 1):
    temp_s = temp_s.replace(str(i), '0')
for i in range(max(no) // 2 + 1, max(no) + 1):
    temp_s = temp_s.replace(str(i), '1')
print(list(map(int, temp_s.split(' '))))
