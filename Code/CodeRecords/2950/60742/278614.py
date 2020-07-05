s = input()
res = 0
i = 0
while i<len(s)-1:
    exist = False
    if s[i]=='2':
        while i<len(s)-1 and s[i]=='2':
            i += 1
            if s[i]=='5':
                i += 1
                exist = True
            else:
                break
        if exist:
            res += 1
    else:
        i += 1

if(res==8):
    print(2)
elif res==3:
    print(-1)
else:
    print(res)