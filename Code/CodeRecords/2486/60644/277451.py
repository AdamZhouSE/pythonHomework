t=int(input())
for k in range(0,t):
    n=input()
    while n.count('[')>0 and n.count(']')>0:
        for i in range(0,len(n)):
            if n[i:i+1]=='[':
                p=1
                for j in range(i+1,len(n)):
                    if n[j:j+1]=='[':
                        p=p+1
                    elif n[j:j+1]==']':
                        p=p-1
                    if p==0:
                        break
                m=int(n[i-1:i])
                n=n[0:i-1]+m*n[i+1:j]+n[j+1:]
                break
    print(n)
