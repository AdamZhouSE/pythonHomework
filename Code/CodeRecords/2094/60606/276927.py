# 有e以外的字母不可以，e两边必须是数字，并且右边必须是整数，正负号后面必须是数字
s = input()
sentinel = 0
for i in range(len(s)):
    # 判断有无e以外的数字
    if s[i] != "e" and "a" <= s[i] <= "z":
        sentinel = 1
        print("False")
        break
    # 当e的时候是否符合规范
    elif s[i] == "e":
        # 左边不是数字
        if i==len(s)-1:
            sentinel = 1
            print("False")
            break
        #右边不是数字
        elif i == 0:
            sentinel = 1
            print("False")
            break
        #两边都是数字
        else:
            #右边是小数
            for j in range(i+1,len(s)):
                if s[j] == ".":
                    sentinel = 1
                    print("False")
                    break9
    elif s[i] == "-" or s[i] == "+":
        if s[i + 1] < "0" or s[i + 1] > "9":
            sentinel = 1
            print("False")
if sentinel == 0:
    print("True")
