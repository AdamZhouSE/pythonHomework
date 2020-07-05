input()
length = list(map(int,input().split(" ")))
target = list(map(int,input().split(" ")))
target.sort()
result = 0
for x in range(target[0]-1,target[1] - 1):
    result += length[x]

if(result > sum(length) - result):
    print(sum(length)-result)
else:
    print(result)