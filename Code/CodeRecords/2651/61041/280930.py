def fun(n):
    string = inttoBinary(n)
    times = int(len(string) / 2)
    new_string = ""
    for i in range(0,times):
        tmp1 = string[i * 2]
        tmp2 = string[i * 2 + 1]
        new_string = new_string + tmp2 + tmp1
    return new_string

def inttoBinary(n):
    string = ""
    while n >= 1 :
        if n% 2==0:
            string = "0" + string
        else:
            string = "1" + string
        n = int(n / 2)

    if len(string) % 2 != 0:
        string = "0" + string  #取到偶数表示
    return string

def bintoInt(string):
    n = 0
    t = 1
    for i in range(0,len(string)):
        if string[len(string) - 1 - i] == "1":
            n = n + t
        t = t * 2
    return n

n = int(input())
for i in range(n):
    m = int(input())
    print(bintoInt(fun(m)))