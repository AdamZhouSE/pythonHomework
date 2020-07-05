table = {"0": 1, "1": 1}
def div(val):
    return val % (pow(10, 9) + 7)

def possibleCount(n):
    if str(n) in table:
        return table[str(n)]
    result = 0
    for i in range(n):
        result += possibleCount(i) * possibleCount(n-i-1)
    table[str(n)] = result
    return result

n = int(input())
p = possibleCount(n)
print(div(p))