T = int(input())
for a in range(0,T):
    n = int(input())
    source = input()
    k = int(input())
    result = source[2*k:]+" "+source[0:2*k]
    print(result)
