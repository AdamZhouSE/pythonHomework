def bf(nums,lower,upper):
    
    import bisect
    from itertools import accumulate
    prefix_sorted_sums = [0]
    ans = 0
    for sums in accumulate(nums):
        left = bisect.bisect_left(prefix_sorted_sums, sums - upper)
        right = bisect.bisect_right(prefix_sorted_sums, sums - lower)
        ans += right - left
        bisect.insort(prefix_sorted_sums, sums)
    print(ans)
if __name__ == '__main__':
    bf(eval(input()),int(input()),int(input()))
