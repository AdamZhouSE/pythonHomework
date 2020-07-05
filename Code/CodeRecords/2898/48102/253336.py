def min_bin(n: int, string: str) -> str:
    a = string.count('0')
    return '1' + '0' * a


num = int(input())
s = input()
print(min_bin(num, s), end='')