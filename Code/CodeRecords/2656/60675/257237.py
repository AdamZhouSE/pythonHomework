def inttoBinary(n):
    string = ""
    while n >= 1 :
        if n% 2==0:
            string = "0" + string
        else:
            string = "1" + string
        n = int(n / 2)
    return string

def compare(n,m):
    if len(n) != len(m):
        if len(n) > len(m):
            for i in range(len(n)-len(m)):
                m = "0" + m
        else:
            for i in range(len(m)-len(n)):
                n = "0" + n
    cnt = 1
    for i in range(0,len(n)):
        if n[len(n)-1-i] != m[len(m)-1-i] :
            break
        cnt = cnt + 1
    if cnt == len(n):
        return -1
    else:
        return cnt

n = int(input())
for i in range(n):
    m = input()
    li = m.split(" ")
    num1 = int(li[0])
    num2 = int(li[1])
    string1 = inttoBinary(num1)
    string2 = inttoBinary(num2)
    print(compare(string1,string2))
