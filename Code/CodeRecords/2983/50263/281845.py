def canBePalindrome(s):
    count = 0
    elements = []
    for i in range(256):
        elements.append(0)
    for i in s:
        elements[ord(i)] += 1
    for i in range(256):
        if elements[i] % 2 == 1:
            count += 1
            if count > 1:
                return False
    return True


def isPalindrome(n, s):
    x = True
    for i in range(n):
        if s[i] != s[n - 1 - i]:
            x = False
            break
    return x


def change(n, s):
    num = 0
    while isPalindrome(n, s) == False:
        for i in range(n):
            if s[i] != s[n - 1 - i]:
                num = num + 1
                k = s[i]

    return num


if __name__ == "__main__":
    n = int(input())
    s = input()
    if canBePalindrome(s):
        if isPalindrome(n, s):
            print("0")
        else:
            print("6")
    else:
        print("Impossible")