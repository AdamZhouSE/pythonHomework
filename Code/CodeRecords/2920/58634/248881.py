#注意读题嗷 是直接切分 而不是挑选后组成序列
n,k = map(int, input().split())
nums = [int(i) for i in input().split(" ")]
deltas = []
for i in range(n-1):
    deltas.append(nums[i+1]-nums[i])
deltas.sort()
result = 0
for i in range(n-k):
    result+=deltas[i]
print(result)