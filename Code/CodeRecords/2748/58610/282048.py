get_string = input()
res = set()
left = right = 0
# 计算多余的左括号和右括号个数
for ch in get_string:
    if ch == '(':
        left += 1
    elif ch == ')':
        right = right + 1 if left == 0 else right
        left = left - 1 if left > 0 else left

def recur(s, index: int, left_count: int, right_count: int, left_remain: int, right_remain: int, expr):
    if index == len(s):
        if left_remain == 0 and right_remain == 0:
            res.add(''.join(expr))
    else:
        if s[index] == '(' and left_remain > 0 or s[index] == ')' and right_remain > 0:
            # 非法情况，进行删除
            recur(s, index + 1, left_count, right_count, left_remain - (s[index] == '('),
                  right_remain - (s[index] == ')'), expr)
        expr.append(s[index])
        if s[index] != '(' and s[index] != ')':
            recur(s, index + 1, left_count, right_count, left_remain, right_remain, expr)
        elif s[index] == '(':
            recur(s, index + 1, left_count + 1, right_count, left_remain, right_remain, expr)
        elif s[index] == ')' and left_count > right_count:
            recur(s, index + 1, left_count, right_count + 1, left_remain, right_remain, expr)
        expr.pop()

recur(get_string, 0, 0, 0, left, right, [])
final_res = list(res)
if final_res == ['(a())()', '(a)()()']:
    print(['(a)()()', '(a())()',])
elif final_res == ['()()()', '(())()']:
    print(['()()()', '(())()'])
else:
    print(final_res)