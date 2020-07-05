import re
s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

# 计算乘除返回值
# 1.使用'*'或者'/'切割,拿到a,b
# 2.计算浮点数a,b结果,返回结果
def atom_cal(exp):
    if '*' in exp:
        a,b = exp.split('*')
        return str(float(a) * float(b))
    elif '/' in exp:
        a,b = exp.split('/')
        return str(float(a) / float(b))

# 格式化--/+-/-+/++等符号,方便计算
def format_exp(exp):
    exp = exp.replace('--','+')
    exp = exp.replace('-+','-')
    exp = exp.replace('+-','-')
    exp = exp.replace('++','+')
    return exp

# 使用正则拿到乘除法算式,再使用atom_exp函数计算乘除法结果,并返回结果
# 1.使用re模块的search方法,筛选乘除法,正则表达式:\d+(\.\d+)?[*/]-?\d+(\.\d+)?
# 2.调用atom_cal函数计算拿到筛选后的乘除算式
# 3.将计算结果替换到原算式位置
# 4.返回计算完结果
def mul_div(exp):
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',exp)
        if ret:
            atom_exp = ret.group()
            res = atom_cal(atom_exp)
            exp = exp.replace(atom_exp,res)
        else:
            return exp

# 使用正则拿到加减进行加减运算
# 1.使用re模块的findall方法,筛选加减法,正则表达式:[+-]?\d+(?:\.\d+)?
# 2.创建结果变量
# 3.拿到所有算式,结果相加
def add_sub(exp):
    ret = re.findall('[+-]?\d+(?:\.\d+)?',exp)
    exp_sum = 0
    for i in ret:
        exp_sum += float(i)
    return exp_sum

# 计算每个算式的结果
# 1.调用乘除法函数(mul_div),先算乘除结果
# 2.格式化计算符号(--/+-/-+/++),方便加减计算
# 3.调用加减法函数(add_sub),计算加减
# 4.返回计算结果
def cal(exp):
    exp = mul_div(exp)
    exp = format_exp(exp)
    exp_sum = add_sub(exp)
    return exp_sum


# 主函数
# 1.去空格
# 2.使用正则拿到所有括号内的算式,正则表达式:\([^()]+\)
# 3.通过re模块的search方法分别取每个算式
# 4.让拿到的括号中的每个算式使用cal函数进行计算
# 5.将计算的结果替换到原算式位置
# 6.解决最外层计算符号
# 7.返回最终计算结果
def main(exp):
    exp = input()
    exp = exp.replace(' ','')
    while True:
        ret = re.search('\([^()]+\)',exp)
        if ret:
            inner_bracked = ret.group()
            res = str(cal(inner_bracked))
            exp = exp.replace(inner_bracked,res)
            exp = format_exp(exp)
        else:
            break
    return cal(exp)
ret = main(s)
print(int(ret))
#print(eval(s))