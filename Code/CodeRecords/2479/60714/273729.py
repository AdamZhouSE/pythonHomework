n = int(input())
for i in range(0, n):
    a = input()
    temp = dict()
    for char in a:
        if char not in temp:
            temp[char] = True
    b = input()
    for char in b:
        if char in temp:
            temp[char] = False
        else:
            temp[char] = True
    ans = ""
    for item in temp:
        if temp[item]:
            ans += item
    print("".join(sorted(ans)))
    print()
