def exchange(n):
    str_n = bin(n)[2:]
    if len(str_n) % 2 == 1:
        str_n = '0' + str_n
    ans = ''
    for i in range(0, len(str_n)//2):
        ans += (str_n[2*i+1]+str_n[2*i])
    return int(ans, 2)


count = int(input())
ans = []
for i in range(0, count):
    num = int(input())
    ans.append(exchange(num))
for j in ans:
    print(j)
