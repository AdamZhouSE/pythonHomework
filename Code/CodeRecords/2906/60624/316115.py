def func16():
    n = int(input())
    a = input().strip()
    n = n%26
    for i in a:
        data = ord(i)
        print(chr(data+n),end="")

    return
func16()