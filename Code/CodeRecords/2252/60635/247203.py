num=int(input())


def comb(src,start,end,res):
    if start== end:
        res.append(''.join(src))
    else:
        for i in range(start,end+1):
            src[start],src[i]=src[i],src[start]
            comb(src,start+1,end,res)
            src[start], src[i] = src[i], src[start]


for i in range(num):
    src=input()
    tar=input()
    repo=[]
    comb(list(tar),0,len(tar)-1,repo)
    ans = 0
    l = len(tar)
    for i in range(len(src) - l + 1):
        if src[i:i + l] in repo:
            ans += 1
    print(ans)