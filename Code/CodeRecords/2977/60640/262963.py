"""
ord() 把ASCII字符转换成对应的值 如"a" 97
chr() 把十进制转换成对应地ASCII码
"""
while True:
    line = input()
    if line == "!":
        break
    li = list(line)
    for i in range(len(li)):
        if 'a' <= li[i] <= 'z':
            dif = ord(li[i])-ord('a')
            res = chr(ord('z')-dif)
            print(res, end="")
        elif 'A' <= li[i] <= 'Z':
            dif = ord(li[i]) - ord('A')
            res = chr(ord('Z') - dif)
            print(res, end="")
        else:
            print(li[i], end="")
    print()
