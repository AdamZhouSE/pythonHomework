"""
子串游戏
注意：
因为可以通过删除字符串中的某个字符来生成子序列，所以不是简单的取子串
思路：
遍历字符串，判断第i位置上的字母是否是元音
如果不是，就继续往后做判断
如果是，就从末尾开始找到辅音，并取出(i,j)这一段字符串
    * 分别删去i+1到j-1位置的元素，然后递归，这样最终可以找到这个字符串所有的子序列
"""


def is_vowel(c):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for v in vowel:
        if c == v:
            return True
    return False


def sub_sequence(string, ans):
    length = len(string)
    for i in range(length):
        if is_vowel(string[i]):
            for j in range(length-1, i, -1):
                if not is_vowel(string[j]):
                    s = string[i:j+1]
                    ans.append(s)
                    for k in range(1, len(s)-1):
                        li = list(s)
                        del li[k]
                        sub_sequence("".join(li), ans)


t = int(input())
for m in range(0, t):
    inp = input()
    answer = []
    sub_sequence(inp, answer)
    res = list(sorted(set(answer)))
    if len(res) > 0:
        for n in range(0, len(res)-1):
            print(res[n], end=" ")
        print(res[len(res)-1])
    else:
        print(-1)
