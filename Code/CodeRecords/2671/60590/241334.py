def cal(w):
    if w==1:
        return 2
    if w==2:
        return 3
    elif w==3:
        return 5
    else:
        w2=2
        w3=3
        for i in range(w-2):
         temp=w2+w3
         w2=w3
         w3=temp
    return temp
t = int(input())
for i in range(t):
    w=int(input())
    print(2**w-cal(w))