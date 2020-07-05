def solve(exp):
    dic = {}
    index = 1
    for str in exp:
        a = str[0]
        b = str[3]
        if '==' in str:
            if a in dic.keys() and b in dic.keys():
                if dic.get(a)!=dic.get(b):
                    return False
            if a in dic.keys() and b not in dic.keys():
                dic[b] = dic.get(a)
            if a not in dic.keys() and b in dic.keys():
                dic[a] = dic.get(b)
            if a not in dic.keys() and b not in dic.keys():
                dic[a]=index
                dic[b]=index
                index = index + 1

        if '!=' in str:
            if a in dic.keys() and b in dic.keys():
                if dic.get(a) == dic.get(b):
                    return False
            if a in dic.keys() and b not in dic.keys():
                dic[b] = index
                index = index + 1
            if a not in dic.keys() and b in dic.keys():
                dic[a] = index
                index = index + 1
            if a not in dic.keys() and b not in dic.keys():
                dic[a]=index
                index = index + 1
                dic[b]=index
                index = index + 1
    return True


if __name__ == '__main__':
    line = input()
    line = line[2:len(line)-2]
    line = line.split('\",\"')
    #print(line)
    if(solve(line)):print("true")
    else:print("false")