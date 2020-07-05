a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    c.sort()
    sum = 0
    for j in range(c.__len__()-2):
        for k in range(j+1,c.__len__()-1):
            for l in range(k+1,c.__len__()):
                if c[j] + c[k] == c[l]:
                    sum += 1
    if sum == 0:
        print(-1)
    else:
        print(sum)