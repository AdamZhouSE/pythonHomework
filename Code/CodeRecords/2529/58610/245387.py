import numpy as np
flag = True
a = int(''.join(map(str, sorted(list(map(int, list(input()))), reverse=True))))
for i in range(int(np.log2(a)) - 3, int(np.log2(a)) + 1):
    if eval(''.join(map(str, sorted(list(str(2 ** i)), reverse=True)))) == a:
        print('true')
        flag = False
        break
if flag:
    print('false')