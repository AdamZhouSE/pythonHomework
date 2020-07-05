def isgood(num, k):
    s = ''
    while num != 0:
        s = str(num%k) + s
        num = int(num / k)
    if s.count('1') == len(s):
        return True
    else:
        return False


n = eval(input())
if str(n).count('0') == len(str(n)) - 1:
    print(n - 1)
    exit()
res = 2
while True:
    if isgood(n, res):
        print(res)
        break
    else:
        res += 1