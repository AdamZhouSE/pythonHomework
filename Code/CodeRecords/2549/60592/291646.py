comd = list(map(int,input().split()))
gems = list(map(int,input().split()))
nums = comd[1]
for i in range(0,nums):
    ls = input().split()
    gems.sort()
    if ls[0]=='1':
        loc = int(ls[1])
        print(gems[len(gems)-loc])
    else:
        v = int(ls[1])
        gems.append(v)