def func():
    now = input()
    while now != "!":
        res = ""
        for ele in now:
            if 65 <= ord(ele) <= 90:
                res += chr(90 - ord(ele) + 65)
            elif 97 <= ord(ele) <= 122:
                res += chr(122 - ord(ele) + 97)
            else:
                res += ele
        print(res)
        now = input()


func()
