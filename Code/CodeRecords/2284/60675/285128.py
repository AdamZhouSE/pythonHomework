def strtoInt(string:str)-> int:
    return int(string)

def func(l: list) -> int:
    MAX_LEN = 1
    for i in range(len(l)):
        for j in range(len(l))[:i:-1]:
            if l[i] < l[j] :
                if j - i > MAX_LEN :
                    MAX_LEN = j - i
                    break
    return MAX_LEN

n = int(input())
for i in range(n):
    num = int(input())
    m = list(map(strtoInt, input().strip().split(" ")))
    print(func(m))
