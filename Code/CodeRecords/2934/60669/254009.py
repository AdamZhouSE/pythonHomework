def decompress(string):
    result=""
    temp=""
    num=""
    i=0
    while i<len(string):
        item=string[i]
        if item != '[' and item != ']':
            if '0'<=item<='9':
                num+=item    # 因为num有可能是两位数
            else:
                temp += item
            i+=1
        else:
            if item=='[':
                comeback=decompress(string[i + 1:])
                temp+=comeback[0]
                i+=comeback[1]
            else:
                if num == "":
                    num = "1"  # 说明没有多个 就变回1
                for x in range(0, int(num)):
                    result += temp
                i+=1
                return result,i+1
    if num == "":
        num = "1"  # 说明没有多个 就变回1
    for x in range(0, int(num)):
        result += temp
    return result,i+1
if __name__ == '__main__':
    string=input()
    print(decompress(string)[0],end="")