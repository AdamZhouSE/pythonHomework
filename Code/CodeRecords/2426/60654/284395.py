a = int(input())
for i in range(a):
    sum = 0
    b = int(input())
    c = list(map(int,input().split()))
    for p in range(0,c.__len__()-2):
        for j in range(p+1,c.__len__()-1):
            for k in range(j+1,c.__len__()):
                if(c[p]*c[j]*c[k]>sum):
                    sum = c[p]*c[j]*c[k]
    print(sum)
