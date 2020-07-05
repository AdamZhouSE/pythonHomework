def f(s):
    left = 0
    right = 0
    # 首先，找到错误的左括号和右括号的数量
    for char in s:
        if char == '(':
            left += 1
        elif char == ')':
            # 没有左括号时，right = right + 1，有左括号时，这个right 和左括号一起消掉
            right = right + 1 if left == 0 else right
            left = left - 1 if left > 0 else left

    result = {}
    def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
        if index == len(s):
            if left_rem == 0 and right_rem == 0:
                ans = "".join(expr)
                result[ans] = 1
        else:
            if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                recurse(s, index + 1, left_count, right_count, left_rem - (s[index]=='('), right_rem-(s[index]==')'), expr)
            expr.append(s[index])
            if s[index] != '(' and s[index] != ')':
                recurse(s, index + 1, left_count, right_count, left_rem, right_rem, expr)
            elif s[index] == '(':
                recurse(s, index + 1, left_count + 1, right_count, left_rem, right_rem, expr)
            elif s[index] == ')' and left_count > right_count:
                recurse(s, index + 1, left_count, right_count + 1, left_rem, right_rem, expr)
            expr.pop()
    recurse(s, 0, 0, 0, left, right, [])
    return list(result.keys())


if __name__ == '__main__':
    line = input()
    print(f(line))
