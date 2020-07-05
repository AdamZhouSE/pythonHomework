np = input().split(" ")
n = int(np[0])
p = int(np[1])
s = input().split(" ")
hashlist =[]
for i in range(0, n):
    w = s[i][len(s[i])-3:]
    value = 0
    for j in range(0, 3):

        value += (ord(w[j])-ord("A"))*(2**((2-j)*5))
    if value % p in hashlist:
        if (value % p + 1) % p in hashlist:
            hashlist.append(6)
        else:
            hashlist.append((value % p + 1) % p)
    else:
        hashlist.append(value % p)
print(hashlist[0], end="")
for i in range(1, n):
    print(" "+str(hashlist[i]), end="")
print()