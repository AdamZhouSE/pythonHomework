#判断名字是否相同
def check1(list:list,name:str):
    for i in list:
        if(list[0] == name):
            return True
    return False
#若名字相同，判断是否有相同email list1是列表的列表，list2是列表
def check2(list1:list,list2:list):
    for i in list1:
        if(check1(i,list2[0]) and hasSame(i,list2)):
            return True
    return False
#判断是否有相同email
def hasSame(list1,list2):
    for i in range(1,len(list1)):
        for j in range(1,len(list2)):
            if list1[i] == list2[j]:
                return True
    return False
    pass

def remove(list : list):
    re = []
    for i in list:
        if i in re:
            pass
        else:
            re.append(i)
    name = re[0]
    re = re[1:len(re)]
    re.sort()
    re.insert(0,name)
    return re
def solve(list):
    result = []
    for i in range(len(list)):
        if check2(result,list[i]):
            for j in range(len(result)):
                if(result[j][0] == list[i][0] and hasSame(result[j],list[i])):
                    for k in range(1,len(list[i])):
                        result[j].append(list[i][k])
                    result[j] = remove(result[j])
        else:
            result.append(list[i])
    return result


if __name__ == '__main__':
    line = input()
    line = line.replace("\", \"","*")
    line = line[1:len(line)-1]
    line = line.split(',')
    str = []
    for s in line:
        s = s.strip()
        s = s[2:len(s)-2]
        str.append(s.split('*'))
    #print(str)
    print(solve(str))