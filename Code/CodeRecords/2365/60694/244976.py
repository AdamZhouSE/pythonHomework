tests = int(input())

for i in range(tests):
    n = int(input())
    l_str = input().split()
    l_str.sort(reverse=True)
    left = -1
    for i in range(n-1):
        if l_str[i][0] == l_str[i+1][0] and len(l_str[i]) > len(l_str[i+1])\
                and l_str[i].count("0") == len(l_str[i])-1:
            if left == -1:
                left = i
            continue
        if left != -1:
            right = i
            l_str[left:right + 1] = list(reversed(l_str[left:right + 1]))
            left = -1

# 反序段在末尾
    if left != -1:
        right = i+1
        l_str[left:right + 1] = list(reversed(l_str[left:right + 1]))  # 反转子数组的方法
        left = -1

    print("".join(l_str))
