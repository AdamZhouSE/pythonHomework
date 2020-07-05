def strtoInt(string:str)-> int:
    return int(string)

def func(l: list) -> int:
    MIN_LEN = len(l)
    for i in range(0, len(l)):  #0 ~ len()-1
        tmp = len(l)
        while tmp > -1:
            t1 = l[i: tmp]
            t = sorted(t1)
            if i == 0 or tmp == len(l):
                if i == 0 and tmp == len(l):
                    total = t
                elif i == 0 and tmp != len(l):
                    total = t + l[tmp: len(l)]
                else:
                    total = l[0: i] + t
            else:
                total = l[0: i] + t + l[tmp: len(l)]
            if total == sorted(l):
                if tmp - i < MIN_LEN :
                    MIN_LEN = tmp - i
            tmp -= 1
    return MIN_LEN


n = "l = " + input()
exec(n)
print(func(l))