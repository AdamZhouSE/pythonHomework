def find_len(nums):
    dic = {}
    for i in nums:
        dic[i] = 1
    lens = []
    for k in nums:
        index = k
        countup = 0
        countdown = 0
        while dic.__contains__(index+1):
            index += 1
            countup += 1
        index = k
        while dic.__contains__(index-1):
            index -= 1
            countdown += 1
        lens.append(countdown+countup+1)
    return max(lens)


if __name__ == "__main__":
    nums = eval(input())
    print(find_len(nums))
    