def isPanlindrome(str):
    i = 0
    j = len(str)-1
    while i < j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    str = input()
    print(isPanlindrome(str))