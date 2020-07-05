def main():
    n = int(input())
    inp = input().split(' ')
    can = []
    for i in range(n):
        can.append(int(inp[i]))
    ability = []
    for a in range(n - 2):
        for b in range(a + 1, n - 1):
            for c in range(b + 1, n):
                pro = can[a] * can[b] * can[c]
                ability.append(pro)
    result = max(ability)
    print(result)


T=int(input())
for i in range(T):
    main()

