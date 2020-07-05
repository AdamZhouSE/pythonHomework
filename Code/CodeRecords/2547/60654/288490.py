a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    d = int(input())
    sum = 0
    for j in range(c.__len__()-1):
        for k in range(j+1,c.__len__()):
            if abs(c[j] - c[k]) == d:
                sum += 1
    print(sum)            