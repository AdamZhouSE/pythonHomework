num=int(input())
s=""
for i in range(num):
    opt=list(input().split(" "))
    if opt[0]=="T":
        s+=opt[1]
    elif opt[0]=="U":
        n=int(opt[1])
        s=s[:len(s)-n:]
    else:
        n = int(opt[1])
        print(s[n-1])