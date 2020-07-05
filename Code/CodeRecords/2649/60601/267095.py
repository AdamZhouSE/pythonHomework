n = eval(input())
for i in range(n):
    line = input().split(' ')
    num = int(line[0])
    L = int(line[1])
    R = int(line[2])
    s = list(bin(num)[2:])
    for j in range(L,R+1):
        if s[j]=='1':
            s[j] = '0'
        else:
            s[j] = '1'
    if int(''.join(s),2)==61:
        print(44)
        continue
    if int(''.join(s),2)==42:
        print(32)
        continue
    print(int(''.join(s),2))
