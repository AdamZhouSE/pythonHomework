T = int(input())
for i in range(T):
    s = int(input())
    count = 0
    while s >0 and (s&(s-1)) >0:
        count+=1
        s&=(s-1)
    print(count+1)