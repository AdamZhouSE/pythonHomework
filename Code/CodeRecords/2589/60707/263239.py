num = int(input())
def lucas(l1):
    if l1 == 0:
        return int(2)
    if l1 == 1:
        return int(1)
    else:
        ans = int(lucas(l1-1) + lucas(l1-2))
        return ans
        
while num > 0:
    inp = input()
    ans = lucas(int(inp))
    print(int(ans))
    num -= 1