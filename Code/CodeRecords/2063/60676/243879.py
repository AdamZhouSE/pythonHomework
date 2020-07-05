def palindrome(num):
    copy = num
    if num < 0:
        return False
    res = 0
    while copy > 0:
        res = res * 10 + copy % 10
        copy //= 10
    return res == num


print(palindrome(int(input())))