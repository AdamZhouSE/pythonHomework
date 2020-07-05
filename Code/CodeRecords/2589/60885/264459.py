table = {"0": 2, "1": 1}

def lucas(n):
    global table
    if str(n) in table:
        return table[str(n)]
    ans = lucas(n-1) + lucas(n-2)
    table[str(n)] = ans
    return ans

def test():
    n = int(input())
    ans = lucas(n)
    result.append(ans)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)
