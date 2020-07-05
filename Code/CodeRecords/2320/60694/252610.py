string = input()
K = int(input())
if K > 1:
    print(''.join(sorted(string)))
    exit()
else:
    res = string
    for i in range(len(string)):
        res = min(res, string[i:] + string[0:i])
    print(res)
