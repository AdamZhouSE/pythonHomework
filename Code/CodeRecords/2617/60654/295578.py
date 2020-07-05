a1 = int(input())
for i in range(a1):
    a,b = map(int,input().split())
    num = 0
    aa = str(a)
    for j in range(aa.__len__()):
        for k in range(j,aa.__len__()):
            if aa[j:k+1].count("1")==b:
                num += 1
    print(num)
