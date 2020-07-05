t=int(intput())
test=[]
for i in range(0,t):
    test.append(input().split())
    mid=list(set(test[i]))
    print(int(''.join(mid)))
