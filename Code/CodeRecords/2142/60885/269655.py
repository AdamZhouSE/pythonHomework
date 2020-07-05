def getNums(line):
    count = 0
    result = []
    left = []
    for c in line:
        if c == '(':
            count += 1
            result.append(str(count))
            left.append(str(count))
        elif c == ')':
            result.append(left.pop(-1))
    return ' '.join(result) + ' '

def test():
    line = input()
    nums = getNums(line)
    return nums

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)