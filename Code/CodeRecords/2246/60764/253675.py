inp=input()
length=len(inp)
i=0
res=False
while True:
    num=int(pow(2,i))
    s=str(num)
    if len(s)==length:
        check=True
        for j in range(len(s)):
            if s[j] not in inp:
                check=False
                break
        if check:
            res=True
            break
    i+=1
    if len(s)>length:
        break
print(res)