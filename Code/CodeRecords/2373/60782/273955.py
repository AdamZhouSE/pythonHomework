"""
题目描述
    斯蒂勒小偷想从一个只有一行房屋的社区中抢钱。他是一个奇怪的人，在洗劫房屋时遵循一定的规则。
    根据规则，他将永远不会抢劫连续两所房子。
    同时，他想最大化他所掠获的数量。
    小偷知道哪所房子有多少钱，但无法提出最佳的抢劫策略。
    如果他严格遵守规则，他会寻求您的帮助，以寻求最大的收益。每个房屋中都有a[i]金额。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    随后是T个测试用例。
    每个测试用例均包含一个整数n，表示房屋数量。
    下一行包含用空格分隔的数字，表示每所房子的钱数
"""
"""
输出描述
    对于每个测试用例，在换行符中，打印一个整数，该整数表示他可以带回家的最大金额。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    nums = list(map(int, input().split(" ")))
    if len(nums) == 0:
        print(0)
    elif len(nums) == 1:
        print(nums[0])
    else:
        select = [0] * len(nums)
        unselected = [0] * len(nums)
        select[0] = nums[0]
        unselected[0] = 0
        for i in range(1, len(nums)):
            select[i] = unselected[i - 1] + nums[i]
            unselected[i] = max(select[i - 1], unselected[i - 1])
        print(max(select[-1], unselected[-1]))