def match_longest_parentheses(s):
    size = len(s)
    li = []  # 记录最长结果的字符串索引，例如：对于"()(()"则返回[[0, 1], [3, 4]]
    deep = 0  # 遇到多少左括号
    start = 0  # 最深的(deep=0 时)左括号的位置
    for i in range(size):
        if s[i] == '(':
            deep += 1
        else:  # s[i] == ')'
            deep -= 1
            if deep == 0:
                if len(li) == 0 or li[0][1] - li[0][0] < i - start:
                    li = [[start, i]]
                elif li[0][1] - li[0][0] == i - start:
                    li.append([start, i])
            elif deep < 0:  # 说明右括号数目大于左括号数目
                deep = 0
                start = i + 1

    deep = 0  # 遇到多少右括号
    start = size - 1  # 最深的(deep=0 时)右括号的位置
    for i in range(size - 1, -1, -1):
        if s[i] == ')':
            deep += 1
        else:  # s[i] == '('
            deep -= 1
            if deep == 0:
                if len(li) == 0 or li[0][1] - li[0][0] < start - i:
                    li = [[i, start]]
                elif li[0][1] - li[0][0] == start - i and not li.__contains__([i, start]):
                    li.append([i, start])
            elif deep < 0:  # 说明左括号数目大于右括号数目
                deep = 0
                start = i - 1
    return li


if __name__ == '__main__':
    s = '()(()))(((((()))'
    li = match_longest_parentheses(s)
    ss = [s[i[0]:i[1] + 1] for i in li]
    answer = len(','.join(ss))
    print(answer)