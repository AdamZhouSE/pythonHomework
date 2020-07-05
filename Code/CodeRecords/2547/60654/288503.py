a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    d = int(input())
    sum = 0
    cc = []
    if d==0:
        for j in range(c.__len__()-1):
            for k in range(j+1,c.__len__()):
                if abs(c[j] - c[k]) == d and c[j] not in cc:
                    sum += 1
                    cc.append(c[j])
    else:
        for k in range(c.__len__()):
            if c[k] not in cc:
                cc.append(c[k])
        c = cc
        for j in range(c.__len__()-1):
            for k in range(j+1,c.__len__()):
                if abs(c[j] - c[k]) == d:
                    sum += 1
    print(sum)