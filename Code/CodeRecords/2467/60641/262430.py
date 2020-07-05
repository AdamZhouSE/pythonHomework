def main():
    time = int(input())
    for i in range(0, time):
        claim = list(map(int, input().split(" ")))
        nums1 = list(map(int, input().split(" ")))
        nums2 = list(map(int, input().split(" ")))
        nums = sorted(nums1 + nums2)
        print(nums[claim[2] - 1])


if __name__ == "__main__":
    main()
