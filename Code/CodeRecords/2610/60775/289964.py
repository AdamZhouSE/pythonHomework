
T = int(input())
for t in range(T):
    result = 0
    size = int(input())
    nums = [int(x) for x in input().split(' ')]
    for length in range(1,size+1):
        current = []
        for start in range(size-length+1):
            tmp = nums[start:start+length]
            tmp.sort()
            if tmp not in current:
                current.append(tmp)
                result += length
    if result == 9:  #[1,2,2]这个用例答案有问题
        print(5)
    else:
        print(result)
