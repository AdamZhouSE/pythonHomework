a=int(input().strip())
for i in range(a):
    length=int(input().strip())
    s=[int(x) for x in input().strip().split()]
    target=int(input().strip())
    if len(s)<4:
        print(0)
    else:
        flag=True
        for x in range(0,len(s)-3):
            if not flag:  
                break
            for y in range(x+1,len(s)-2):
                if not flag:
                    break
                for p in range(y+1,len(s)-1):
                    if not flag:
                        break
                    for q in range(p+1,len(s)):
                        if not flag:
                            break
                        if s[x]+s[y]+s[p]+s[q]==target:
                            print(1)
                            flag=False
                            break
        if flag:
            print(0)