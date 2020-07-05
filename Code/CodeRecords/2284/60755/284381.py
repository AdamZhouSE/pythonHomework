num = int(input())
for i in range(num):
    n  = int(input())
    all = input().split(" ")
    res = []
    for k in range(len(all)):
        all[k] = int(all[k])
    for a in range(len(all)):
        for b in range(a+1,len(all)):
            if all[a]<all[b]:
                res.append(b-a)
    result = max(res)     
    if result ==4:
        print(all)
    print(result)