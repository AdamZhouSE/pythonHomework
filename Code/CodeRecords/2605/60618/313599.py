class Solution:
    def find(self, n, hp, ords):
        for o in ords:
            if o[0] == 1:
                x = o[1]
                y = o[2]
                xi = -1
                yi = -1
                for i in range(len(hp)):
                    if nums[x-1] in hp[i]:
                        xi = i
                    elif nums[y-1] in hp[i]:
                        yi = i
                if xi != -1 and yi != -1:
                    hp[xi] = set.union(hp[xi], hp[yi])
                    del hp[yi]


            elif o[0] == 2:
                x = o[1]
                xi = -1
                for i in range(len(hp)):
                    if nums[x-1] in hp[i]:
                        xi = i
                if xi != -1:
                    m = min(hp[xi])
                    print(m)
                    hp[xi].remove(m)
                else:
                    print(-1)


if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]
    hp = [{int(a)} for a in input().split()]
    global nums
    nums = []
    for i in range(len(hp)):
        nums.append(hp[i].copy().pop())
    ords = []
    for i in range(m):
        ords.append([int(a) for a in input().split()])
    s = Solution()
    res = s.find(n, hp, ords)
