def largestDivisibleSubset(nums):
    s = {-1: set()}
    for n in sorted(nums):
        s[n] = max((s[d] for d in s if n % d == 0), key=len) | {n}
    return list(max(s.values(), key=len))

def main():
    list0 = list(map(int,input().split(",")))
    list1 = largestDivisibleSubset(list0)
    list1.sort()
    print(list1)
if __name__ == '__main__':
    main()
