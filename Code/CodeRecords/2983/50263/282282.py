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
    k = 0
    sum = 0
    string = ''
    m = ''
    lists = list(s)
    elements = []
    for i in range(256):
        elements.append(0)
    for i in s:
        elements[ord(i)] += 1
    for i in range(256):
        if elements[i] % 2 == 1:
            k = (elements[i] + 1)/2
            m = chr(i)
            break
    for i in range(n):
        if lists[i] == m:
            sum += 1
            if sum == k:
                num += abs(i-int(n/2))
                del lists[i]
    string = string.join(lists)
    for i in range(int(len(string)/2)):
        if string[i] != string[len(string)-1-i]:
            char = string[i]
            for j in range(len(string)-1-i, -1, -1):
                if string[j] == char:
                    num += len(string)-j-i-1
                    string = string[0:j] + string[j+1:len(string)-i] + char + string[len(string)-i:len(string)]
                    break
    return num


if __name__ == "__main__":
    n = int(input())
    s = input()
    if canBePalindrome(s):
        if isPalindrome(n, s):
            print("0")
        else:
            print(change(n, s))
    else:
        print("Impossible")

