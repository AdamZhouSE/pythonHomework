n = int(input())
nums_str = list(input().split(' '))
nums = [int(num) for num in nums_str]

def shuffle(i, j):
    count = 0
    index = i
    for k in range(i, j):
        if count % 2 == 1:
            nums.insert(index, nums.pop(k))
            index += 1
        count += 1
    
def solve():
    count = 0
    ans = list()
    flag = True
    while flag:
        start = 0
        end = 0
        flag = False
        i = 0
        while i + 1 < n:
            if nums[i] > nums[i + 1] and not flag:
                start = i
                i += 2
                flag = True
            elif nums[i] < nums[i + 1] and flag:
                end = i
                break
            elif flag:
                i += 2
            elif not flag:
                i += 1
        if i + 1 == n or i == n:
            end = n
        if flag:
            count += 1
            ans.append([start, end])
            shuffle(start, end)

    print(count)
    for a in ans:
        print(a[0] + 1, a[1], sep=' ')

solve()