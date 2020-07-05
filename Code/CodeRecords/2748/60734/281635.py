def isvalid(string):
    lst = []
    for i in range(len(string)):
        if string[i] == '(':
            lst.append(string[i])
        elif string[i] == ')':
            if len(lst) != 0 and lst[-1] == '(':
                lst.pop()
            else:
                return False
    return lst==[]

string = input()
level = {string}
while True:
    valid = list(filter(isvalid,level)) #筛选出合格解，如果不为空，打印，break
    if valid:
        print(valid)
        break
    next_level = set()  #避免重复解
    for item in level:
        for i in range(len(item)):
            if item[i] in "()":
                next_level.add(item[:i]+item[i+1:]) #删除每一个元素的结果，在下一循环中逐一检验
    level = next_level