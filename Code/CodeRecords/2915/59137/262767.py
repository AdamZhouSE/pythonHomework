def s24():
    n = int(input())
    nums = list(input().split())

    for i in range(n):
        nums[i] = int(nums[i])

    count = 1
    answer = 1

    for i in range(1, n):
        if nums[i] > 2*nums[i-1]:
            if count > answer:
                answer = count
            count = 1
        else:
            count = count + 1

    if count > answer:
        answer = count
    print(answer)


s24()