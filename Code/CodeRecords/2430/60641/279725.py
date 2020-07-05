def main():
    num = int(input())
    for i in range(0, num):
        length = int(input())
        nums = list(map(int, input().split(" ")))
        destination = int(input())
        temp = length
        while length > 0:
            one = nums[0]
            del nums[0]
            the_other = destination - one
            if the_other in nums:
                print(str(one) + " " + str(the_other) + " " + str(destination))
                nums.remove(the_other)
                length -= 2
            else:
                nums.append(one)
                length -= 1
                continue
        if len(nums) == temp:
            print(-1)


if __name__ == '__main__':
    main()
