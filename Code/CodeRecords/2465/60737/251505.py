def h_index(citations):
    l, n, r = 0, len(citations), len(citations)-1
    while l < r:
        mid = (l + r + 1) >> 1
        if citations[mid] <= n - mid:
            l = mid
        else:
            r = mid - 1
    if l < n and n - l > citations[l]:
        return n - l - 1
    return n - l


if __name__ == "__main__":
    nums = [int(n) for n in input().split(',')]
    print(h_index(nums))