t=int(input())
test=[]
mid=[]
for i in range(0,t):
    test.append(list(input()))
    mid=list(set(test[i]))
    print(int(''.join(mid)))
    test=[]
