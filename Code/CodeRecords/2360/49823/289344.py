def dw(A):
    import collections
    def backtrace(remain, cur_arr):
        if not remain:
            return 1
        ans = 0
        for num in list(remain):
            s = num if not cur_arr else num + cur_arr[-1]
            if not cur_arr or int(s ** 0.5) ** 2 == s:
                remain[num] -= 1
                if remain[num] == 0:
                    del remain[num]
                ans += backtrace(remain, cur_arr + [num])
                remain[num] += 1
        return ans
    print(backtrace(collections.Counter(A), []))
if __name__ == '__main__':
    dw([int(i) for i in input().split(',')])
