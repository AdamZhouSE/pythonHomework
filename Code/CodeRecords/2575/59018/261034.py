def effectiveBracket(string):
    resString = string[::-1]        #字符串反转
    lista = []                      #定义一个空列表
    for stra in resString:          #这个循环的作用就是将括号进行相应改变
        if stra == "{":
            lista.append("}")          #将改变后的括号添加到列表
        elif stra == "}":
            lista.append("{")
        elif stra == "(":
            lista.append(")")
        elif stra == ")":
            lista.append("(")
        elif stra == "[":
            lista.append("]")
        elif stra == "]":
            lista.append("[")
    replaceString = "".join(lista)  #将改变后的字符合并成一个字符串
    if replaceString == string:     #判断改造后的字符串与原始字符串是否相等
        return True
    else:
        return False

print(effectiveBracket("{()}"))
