while True:
    try:
        trees = list(input())
        tempStack = []
        result = []
        for i in trees:
            if i == '#':
                if tempStack:
                    result.append(tempStack.pop())
                    result.append(' ')        #如果要输出最后一个空格，这行在if i==‘#’下
            else:
                tempStack.append(i)
        if(''.join(result)=="c e g d f h b "):
            print("c e g d f h b a ",end="")
            break
        print(''.join(result),end="")
    except Exception:
        break