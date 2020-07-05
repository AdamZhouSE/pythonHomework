def get_height(s, a, b):
    strs = []
    for i in range(a, b+1):
        strs.append(s[:i])
    count = 0
    n = len(strs)
    for j in range(n-1):
        for k in range(j+1, n):
            s1 = strs[j]
            s2 = strs[k]
            m = 0
            max = 0
            while m<len(s1):
                if s1[-1-m] == s2[-1-m]:
                    max += 1
                    m += 1
                    if m == len(s1):
                        count = max if max > count else count
                else:
                    count = max if max > count else count
                    m = len(s1)

    return count


if __name__ == "__main__":
    m = [int(n) for n in input().split( )][1]
    s = input()
    while m > 0:
        nums = [int(n) for n in input().split( )]
        print(get_height(s, nums[0], nums[1]))
        m -= 1
