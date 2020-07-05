def isValid(edges):
    if edges[0] <= edges[2] - edges[1]:
        return False
    if edges[2] >= edges[0] + edges[1]:
        return False
    return True

def test():
    l = int(input())
    nums = list(map(int, input().split()))
    pos = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                edges = sorted([nums[i], nums[j], nums[k]])
                if isValid(edges) and edges not in pos:
                    pos.append(edges)
    result.append(len(pos))

result = []
for t in range(int(input())):
    test()

for line in result:
    print(line)