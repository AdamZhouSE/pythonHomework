def is_char(ch):
    if '0' <= ch <= '0':
        return True
    if 'a' <= ch <= 'z':
        return True
    if 'A' <= ch <= 'Z':
        return True
    return False

def is_palindrome(str):
    i = 0
    j = len(str)-1
    n = len(str)
    while i < j:
        while i<n and (not is_char(str[i])):
            i = i + 1
        while j>=0 and (not is_char(str[j])):
            j = j - 1
        if i >= n:
            for k in range(j,-1,-1):
                if is_char(str[k]):
                    return False
            return True
        if j < 0:
            for k in range(i,n):
                if is_char(str[k]):
                    return False
            return True
        if str[i] != str[j]:
            return False
        i = i + 1
        j = j - 1
    return True

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        str = input()
        ans.append(is_palindrome(str.lower()))
    for res in  ans:
        if res:
            print('YES')
        else:
            print('NO')