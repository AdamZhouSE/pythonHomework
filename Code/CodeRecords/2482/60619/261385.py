import math
t = int(input())
for ind in range(t):
    up = int(input())
    down = int(input())
    if down % 3 == 0 and up % 3 != 0:
        result = [str(int(up / down)), "."]
        up = up % down * 10
        end = 1
        while str(int(up/down)) != result[end]:
            result.append(str(math.floor(up/down)))
            up = (up % down)*10
            end += 1
        result.insert(end, "(")
        result.append(")")
        print(''.join(result))
    else:
        print(up/down)