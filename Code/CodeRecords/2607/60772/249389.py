import sys

def execute(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            sub = s[i:j + 1]
            if len(sub) % 3 == 0:
                if sub.count('1') == sub.count('2') == sub.count('0'):
                    count += 1
    return count



Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    s = Input[begin]
    begin += 1
    print(execute(s))
