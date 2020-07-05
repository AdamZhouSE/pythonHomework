def valid(line):
    ans = 0
    stack = 0
    temp = 0
    for c in line:
        if c == '(':
            stack += 1
            temp += 1
        elif c == ')':
            if stack == 0:
                break
            else:
                stack -= 1
                temp += 1
        if stack == 0 and temp > ans:
            ans = temp
    return ans

def find_longest_valid(line):
    ans = 0
    for i in range(len(line)):
        temp = valid(line[i:])
        if temp > ans:
            ans = temp
    return ans

def test():
    line = input()
    A.append(find_longest_valid(line))

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)