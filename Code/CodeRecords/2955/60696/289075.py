K = 0


def get_char_distance(a,b):
    if (ord(a) == ord(' ') and ord(b) != ord(' ')) or (ord(b) == ord(' ') and ord(a) != ord(' ')):
        return K
    else:
        return abs(ord(a) - ord(b))


def get_str_distance(str1, str2):
    n = len(str1)
    m = len(str2)
    distance = [[0 for i in range(m+1)] for i in range(n+1)]    # distance[i][j]表示str1前i个元素到str2前j个元素的距离
    for j in range(m+1):    # 初始化, 空到前j个元素的距离为K*j
        distance[0][j] = K * j
    for i in range(n+1):    # 初始化, 空到前i个元素的距离为K*i
        distance[i][0] = K * i
    for i in range(1, n+1):
        for j in range(1, m+1):
            distance[i][j] = max(distance[i-1][j-1]+get_char_distance(str1[i-1], str2[j-1]), distance[i-1][j]+K,
                                 distance[i][j-1]+K)
    return distance[n][m]


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    K = int(input())
    print(get_str_distance(str1, str2))
