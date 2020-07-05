nums = int(input())
for i in range(0,nums):
    total = int(input())
    ls = list(map(int,input().split(' ')))
    ls.sort()
    for j in range(0,total):
        if ls[j]<=0:
            continue
        else:
            if 1 in ls:
                if j<total-1 and ls[j+1]-1==ls[j]:
                    continue
                else:
                    print(ls[j]+1)
                    break
            else:
                print(1)
                break