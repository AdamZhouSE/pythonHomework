def getPos(pos, total, next):
    if len(next) == 0:
        pos.append(total)
    else:
        for i in range(len(next)):
            if i >= len(next)-2:
                getPos(pos, total+next[i], [])
            else:
                getPos(pos, total+next[i], next[i+2:])

def test():
    n = int(input())
    nums = list(map(int, input().split()))
    pos = []
    getPos(pos, 0, nums)
    result.append(max(pos))

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)