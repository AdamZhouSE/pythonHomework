def balance(line):
    if len(line) % 2 == 1:
        return -1
    left = 0
    count = 0
    for c in line:
        if c == '{':
            left += 1
        elif c == '}':
            if left == 0:
                count += 1
                left += 1
            else:
                left -= 1
    return count + int(left/2)

def test():
    line = input()
    return balance(line)

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)