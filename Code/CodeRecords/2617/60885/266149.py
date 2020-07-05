def count(nums, k):
    ans = 0
    for i in range(0, len(nums)-k):
        ans += nums[i] * nums[i+k]
    return ans
    
def bit_to_count(line):
    counter = []
    count = 1
    for c in line:
        if c == '1':
            counter.append(count)
            count = 1
        elif c == '0':
            count += 1
    counter.append(count)
    return counter

def test():
    line,k = input().split()
    nums = bit_to_count(line)
    result = count(nums, int(k))
    A.append(result)

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)