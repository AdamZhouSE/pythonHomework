s = input()
sz = len(s)
# length
dp = [[sz + 1] * sz for i in range(sz)]
strings = [[''] * sz for i in range(sz)]
for i in range(sz):
    dp[i][i] = 1
    strings[i][i] = s[i]


# def solve(left, right):


def check(begin, end, length):
    if (end - begin + 1) % length != 0:
        return False

    for i in range(end - begin + 1):
        if s[begin + i] != s[begin + i % length]:
            return False
    return True


for gap in range(1, sz):  # 区间长度
    begin = 0
    while begin + gap <= sz - 1:
        # while begin + 2 * gap + 1 <= sz - 1:
        for i in range(gap):
            if dp[begin][begin + i] + dp[begin + i + 1][begin + gap] < dp[begin][begin + gap]:
                dp[begin][begin + gap] = dp[begin][begin + i] + dp[begin + i + 1][begin + gap]
                strings[begin][begin + gap] = strings[begin][begin + i] + strings[begin + i + 1][begin + gap]
        for length in range(1, gap):
            if check(begin, begin + gap, length):
                times = (gap + 1) // length
                # if begin == 0:
                repeatStr = str(s[begin:begin + length])
                # else:
                #     repeatStr = str(s[begin - 1:begin + length - 1])

                temp = str(times) + '(' + repeatStr + ')'
                if len(temp) < dp[begin][begin + gap] or (
                        len(temp) == dp[begin][begin + gap] and temp < strings[begin][begin + gap]):
                    dp[begin][begin + gap] = len(temp)
                    strings[begin][begin + gap] = temp
        begin += 1
print(strings[0][sz-1])