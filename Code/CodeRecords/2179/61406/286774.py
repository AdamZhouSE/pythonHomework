nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
s = input()
for i in range(0,m):
    abcd = input().split(' ')
    a = int(abcd[0])
    b = int(abcd[1])
    c = int(abcd[2])
    d = int(abcd[3])
    str1=s[a-1:b]
    str2=s[c-1:d]
    maxlength = 0
    for j in range(len(str2),0,-1):
        if str1.count(str2[0:j])!=0:
            maxlength = j
            break
    print(maxlength)