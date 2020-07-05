"""
题目描述
    给定一个正整数，返回它在 Excel 表中相对应的列名称。
"""
a = int(input())
answer = ""
while a > 0:
    if a % 26 != 0:
        answer += chr(a % 26 + 64)
    else:
        answer += 'Z'
        a //= 26
    a //= 26
ans = list(answer)
ans.reverse()
# print(ans)
print("".join(ans))