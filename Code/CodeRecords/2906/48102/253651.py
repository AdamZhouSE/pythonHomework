def code(n: int, string: str) -> str:
    res = ''
    for i in string:
        res += chr((ord(i)-97+n) % 26+97)
    return res


num = int(input())
s = input()
print(code(num, s), end='')

