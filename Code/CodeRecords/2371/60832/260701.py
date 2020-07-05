All = int(input())

for q in range(All):
    isPalindrome = True
    s = input().lower()
    length = len(s)

    a = 0
    b = length - 1

    while a < b:
        while not s[a].isalpha():
            a += 1
        while not s[b].isalpha():
            b -= 1

        if s[a] != s[b]:
            isPalindrome = False
            break
        a += 1
        b -= 1

    if isPalindrome:
        print('YES')
    else:
        print('NO')
