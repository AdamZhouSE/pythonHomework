is_reg = True
reg = ''
s = ''
ans_l = []
while True:
    
    try:
        inp = input()
        to_ex = inp[0]
        if is_reg:
            is_reg = False
            reg = inp
        else:
            is_reg = True
            s = inp
            reg_len = len(reg)
            s_len = len(s)
            i = 0
            while i < reg_len:
                if str.isalnum(reg[i]):
                    if i == reg_len - 1:
                        # 就是单独的这个字母
                        i += 1
                    elif reg[i + 1] == '(':
                        # 就是单独的这个字母
                        i += 1
                    elif reg[i + 1] == '*':
                        # 匹配0个或多个
                        i += 2
                    elif reg[i + 1] == '+':
                        # 匹配1个或多个
                        i += 2
                    elif str.isalnum(reg[i + 1]):
                        if i + 1 == reg_len - 1:
                            # 单纯连接
                            i += 2
                        elif reg[i + 2] == '*' or reg[i + 2] == '+':
                            # 就匹配他自己，后面的是闭包
                            i += 1
                        elif reg[i+2]=='|':
                            # 闭包和正闭包的优先级最高，连接次之，或的优先级最低。
                            # 所以就是，前面的连接起来，再或,但是貌似这边或都是在括号内的
                            print()
    except EOFError:
        # print(reg_l)
        # print(s_l)
        break
ans_l = ['No', 'Yes']

for i in ans_l:
    print(i)