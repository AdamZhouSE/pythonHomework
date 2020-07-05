def cal(w):
    if w==1:
        return 1
    if w==2:
        return 2
    elif w==3:
        return 3
    else:
        w2=2
        w3=3
        for i in range(w-3):
         temp=w2+w3
         w2=w3
         w3=temp
    return temp
t = int(input())
for i in range(t):
    w=int(input())
    print(cal(w))


