def dp(a, num):
    max_len = 1
    for i in range(len(a)):
        tmp_len = 1
        for j in range(i + 1, len(a)):
            if a[j] - a[i] == tmp_len * num:
                tmp_len += 1
        max_len = max(max_len, tmp_len)
    return max_len


if __name__ == '__main__':
    a = list(eval(input()))
    print(dp(a, int(input())))
