def decode(code):
    left = [] #记录左括号位置
    for i in range(0,len(code)):
        if(code[i]=='['):
            left.append(i)
    for i in range(len(left)-1,-1,-1):
        size = 2  #要替换的串的长度（初始为[]，之后为展开后的长度）
        num = 0  #被压缩的次数
        temp = ""  #记录当前被展开的串
        now = ""
        j = left[i]+1 #左括号的下一个字符
        while(code[j]!=']'):
            if(code[j].isdigit()):
                num = num*10+int(code[j])  #数字可能不止一位
            else:
                temp += code[j]
                size += 1
            j +=1
        for x in range(num):
            now += temp
        code = code[:left[i]] + now + code[left[i]+size+1:]
    return code

code = input()
if(decode(code)[-1]==']'):
    print(decode(code)[:-1],end="")
else:
    print(decode(code), end="")

