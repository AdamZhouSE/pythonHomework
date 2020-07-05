def getNum(o_str, code):
    num = 0
    for i in range (len(o_str) - len(code) + 1):
        tmp = o_str[i:i + len(code)]
        if sorted(list(tmp)) == sorted(list(code)):
            num += 1
    return num

if __name__ == '__main__':
    s = input()
    ctr = int(input())
    total_num = 0
    code_list = []
    for i in range(ctr):
        code = input()
        code_list.append(code)
        total_num += getNum(s, code)
    
    print(total_num)




