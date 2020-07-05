# 传入一个字符串,递归实现
# python中的或且非是 or and not


def recursion(string):
    if int(string) <= 100 or len(string) <= 2:
        return int(string)
    else:
        new_s = ""
        s_list = list(string)
        for i in range(0, len(string)-1):
            num = int(s_list[i]) + int(s_list[i+1])
            if num >= 10:
                # 取得和的个位数
                num %= 10
            new_s += str(num)
        return recursion(new_s)


s = input()
ST = int(input())
li = list(s)
luck = []
# ord() 把字符转换为ASCII值，chr()正好相反
# str() 把对象转换为字符串形式
for c in li:
    luck.append(str(ord(c)-ord('A')+ST))
li1 = "".join(luck)
result = recursion(li1)
print(result, end='')

