def isSame(str1:str,str2:str):
    if str1==str2:
        return True
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            s = list(str1)
            temp = s[i]
            s[i] = s[j]
            s[j] = temp#交换两个位置的字符
            if s == list(str2):
                return True
    return False

def solve(list:list):
    re = [] #列表的列表
    re.append([list[0]])
    for i in list:
        logo = False
        for j in range(len(re)):
            for k in range(len(re[j])):
                if isSame(i,re[j][k]):
                    logo = True
                    if i!=re[j][k]:
                        re[j].append(i)

        if logo == False:
            re.append([i])
    return len(re)

if __name__ == '__main__':
    line = input()
    line = line[2:len(line)-2]
    line = line.split('\",\"')
    #print(line)
    print(solve(line))