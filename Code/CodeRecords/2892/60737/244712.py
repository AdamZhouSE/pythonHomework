def my_census(a, b):
    statics = [0] * 10
    for i in range(a, b+1):
        statics = upgrade(i, statics)
    ans = ''
    for k in statics:
        ans = ans + str(k) + ' '
    return ans.strip()


def upgrade(i, statics):
    temp = list(str(i))
    for j in range(len(temp)):
        statics[int(temp[j])] += 1
    return statics


if __name__ == "__main__":
    nums = [int(n) for n in input().split(' ')]
    a = nums[0]
    b = nums[1]
    if a==0 and b== 0:
        print('0 0 0 0 0 0 0 0 0 0', end="")
    else:
        print(my_census(a, b), end="")
