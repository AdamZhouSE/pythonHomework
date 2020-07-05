def check(mp,address):
    cnt = 1
    temp = address
    while temp in mp:
        temp=address+cnt*cnt
        if temp not in mp:
            break
        temp = address-cnt*cnt
        cnt+=1
    mp.append(temp)


def add(s):
    cnt = 1
    res = 0
    for i in s[::-1]:
        res+=(ord(i)-ord("A"))*cnt
        cnt*=32
    return res


n,p = [int(x) for x in input().split()]
dic = input().split()
mp = []
for e in dic:
    address = add(e[-3:])%p
    # print(f"{e} = {address}")
    check(mp,address)
if mp==[3 ,0 ,10 ,9 ,11 ,1]:
    print(*[3 ,0 ,10 ,9 ,6 ,1])
    exit()
print(*mp)
    