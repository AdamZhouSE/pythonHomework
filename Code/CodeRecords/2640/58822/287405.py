def pai(a):
    b=list(a)
    b.sort()
    s="".join(b)
    return s
n=input()
target=input()
num=10000
s=""
t=pai(target)
for i in range(0,len(n)):
    for k in range(i+1,len(n)):
        if(pai(n[i:k])==t):
            if(len(n[i:k])<num):
                num=len(n[i:k])
                s=n[i:k]
if(s==""):
    print("BANC")
else:
    print(s)