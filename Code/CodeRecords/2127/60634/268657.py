def solve(a,b):
    res = 1
    bit = 1
    i = len(b)-1
    while i >= 0:
        temp = int(pow(a,b[i]))%1337
        res *= int(pow(temp,bit))
        res %= 1337
        bit *= 10
        i -= 1
    print(res)
    
#main-----
a = int(input())
b = [int(x) for x in input().split(",")]
solve(a,b)

