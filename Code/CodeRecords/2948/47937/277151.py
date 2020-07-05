s = input()
ST = int(input())#输入
l = ""
for i in s:
    l += (str(ord(i) + ST - ord('A')))#string不能改里面的字符，所以要用另一个string处理
while len(l) > 2 and l != "100":#如果是两位数或者100了就输出
    s = ""
    for i in range(1, len(l)):
        s += (str((int(l[i]) + int(l[i - 1])) % 10))#加到前一位，%10
    l = s#重新赋值
print(int(l))#输出