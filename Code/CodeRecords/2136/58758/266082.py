def isvalid(num, base):
    if num == 1:
        return True
    factor = 1
    while factor < num:
        factor = factor*base+1
    if factor == num:
        return True
    else:
        return False


n = int(input())
ans = 2
while True:
    if isvalid(n, ans):
        print(ans)
        break
    ans += 1
