

def solve():
    str1 = input()
    str2 = ']'
    index = str1.index(str2)
    tmp = str1[8:index]
    tmp_list = tmp.split(',')
    nums = []
    for i in range(0,len(tmp_list)):
        nums.append(int(tmp_list[i]))
    index_k = str1.index('k')
    index_t = str1.index('t')
    a = index_k + 3
    b = index_t + 3
    tmp_k = ''
    while str1[a] != ',':
        tmp_k += str1[a]
        a = a + 1
    k = int(tmp_k)
    t = int(str1[b:])
    res = 'false'
    for i in range(0,len(nums)):
        for j in range(1,k + 1):
            if i + j == len(nums):
                break
            if abs(nums[i + j] - nums[i]) <= t:
                print('true')
                return
    print(res)

solve()