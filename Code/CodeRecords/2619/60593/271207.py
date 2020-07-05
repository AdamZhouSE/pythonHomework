t=int(input())
for _ in range(t):
    n=input()
    ans=set()
    ok=1
    for i in range(len(n)):
        for j in range(i+1,len(n)+1):
            ss=n[i:j]
            tmp=1
            for k in ss:
                tmp*=ord(k)-ord('0')
            if(tmp in ans):
                ok=0
                break
            else:
                ans.add(tmp)
    print(ok)