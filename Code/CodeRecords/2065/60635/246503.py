src=input()


def atoi(src):
    src=src.replace(' ','')
    sign = ''
    if src[0] == '-' or src[0]=='+':
        sign=src[0]
        src=src[1:]
    num=[]
    for i in range(len(src)):
        if src[i].isdigit():
            num.append(src[i])
        else:
            break
    if len(num)==0:
        return 0
    return int(sign+''.join(num))

ans=atoi(src)
if -2**31<=ans<=2**31-1:
    print(ans)
else:
    print(-2**31 if ans<0 else 2**31-1)


