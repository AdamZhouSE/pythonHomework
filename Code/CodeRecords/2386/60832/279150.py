All = int(input())

for q in range(0, All):
    length = int(input())
    ar = list(map(int, input().split()))
    x=int(input())

    has=0

    for i in range(0,length-3):
        for j in range(i+1, length - 2):
            for k in range(j+1, length - 1):
                for l in range(k+1, length):
                    if ar[i]+ar[j]+ar[k]+ar[l]==x:
                        has=1
                        print(has)
                        exit()

    print(has)