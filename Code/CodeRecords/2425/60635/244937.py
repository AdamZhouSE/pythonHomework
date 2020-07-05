count = int(input())
for n in range(count):
    info = input().split()
    n = int(info[0])
    k = int(info[1])
    arr = [int(x) for x in input().split()]
    if k in arr:
        print(k)
    else:
        ans=[]
        have_found=False
        diff = 1
        while not have_found:
            for a in arr:
                if abs(a-k)==diff:
                    ans.append(a)
            if len(ans)>0:
                have_found=-True
            diff += 1
    print(max(ans))
        