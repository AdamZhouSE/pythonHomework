#分治法
def calculate(string):
    res = [] #用于存放当前式子所有可能的结果
    for i in range(len(string)):
        if string[i].isdigit() == False: #找到操作符
            for left in calculate(string[:i]): #递归计算操作符左边式子所有的可能值
                for right in calculate(string[i+1:len(string)]): #递归计算操作符右边式子所有的可能值
                    if string[i] == '+':
                        output = left+right
                    elif string[i] == '-':
                        output = left-right
                    elif string[i] == '*':
                        output = left*right
                    res.append(output)
    if len(res) == 0:
        res.append(int(string))
    return res

s = input()
print(calculate(s))