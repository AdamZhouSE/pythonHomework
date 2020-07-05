# 题目描述
# 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，
# 总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
#
# 注意:
# 字符串长度 和 k 不会超过 104。

# 滑动窗口法

if __name__ == '__main__':
    string = input().strip()
    string = list(string)
    k = int(input())
    begin = 0
    diction = dict()
    if k >= len(string):
        print(k)
    else:
        end = k
        for i in list("QWERTYUIOPASDFGHJKLZXCVBNM"):
            diction[i] = 0
        for i in range(begin, end+1):
            diction[string[i]] += 1
        newd = diction.items()
        newd = sorted(newd, key=lambda vi: vi[1], reverse=True)
        if newd[0][1] + k >= len(string):
            print(len(string))
        else:
            maxLen = 0
            while end < len(string):
                newd = diction.items()
                newd = sorted(newd, key=lambda vi: vi[1], reverse=True)
                maxDuplicated = newd[0][1]
                if maxDuplicated + k > end - begin + 1:
                    if end+1 < len(string):
                        diction[string[end+1]] += 1
                        end += 1
                    else:
                        end += 1
                elif maxDuplicated + k < end - begin + 1 :
                    diction[string[begin]] -= 1
                    begin += 1
                else:
                    maxLen = max(maxLen,  end - begin + 1)
                    if end + 1 < len(string):
                        diction[string[end + 1]] += 1
                        end += 1
                    else:
                        end += 1
            print(maxLen)
