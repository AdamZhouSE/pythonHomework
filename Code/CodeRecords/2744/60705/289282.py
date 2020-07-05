# 判断字符串是否回文
def judge(string):
    l = len(string)
    if l == 1:
        return True
    else:
        for i in range(0, l // 2):
            if string[i] != string[l-1-i]:
                return False
        return True


if __name__ == '__main__':
    n = int(input())
    s = []
    for i in range(0, n):
        s.append(input().split(" ")[1])
    count = 0
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            if judge(s[i]+s[j]):
                count += 1
    print(count)
