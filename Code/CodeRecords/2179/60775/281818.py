input1 = input().split(' ')
slen = int(input1[0])
num_que = int(input1[1])
s = input()
for M in range(num_que):
    tmp = input().split(' ')
    a = int(tmp[0])
    b = int(tmp[1])
    c = int(tmp[2])
    d = int(tmp[3])

    maxlen = 0
    for length in range(b-a+2):
        pre = s[a:a+length]
        if length > d-c+1:
            break
        if pre == s[c:c+length]:
            maxlen = max(maxlen,length)

    print(maxlen)
