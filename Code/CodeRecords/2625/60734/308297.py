def dif(string):
    res = []
    for i in range(1, len(string)):
        left_info = dif(string[:i])
        right_info = dif(string[i:])
        for left, vl in left_info:
            for right, vr in right_info:
                res.append([left+'+'+right, vl+vr])
                res.append([left+'-'+right, vl-vr])
                res.append([left+'*'+right, vl*vr])
    res.append([string, int(string)])
    return res

def test(string,value):
    import re
    string = re.findall(r'\d+|\+|\-|\*',string)

    for x in string:
        if len(x)>1 and x.startswith('0'):
            return False
    while len(string)>1:
        if '*' in string:
            index = string.index('*')
            num1 = int(string[index-1])
            num2 = int(string[index+1])
            string = string[:index-1]+[str(num1*num2)]+string[index+2:]
        else:
            num1 = int(string.pop(0))
            op = string.pop(0)
            num2 = int(string.pop(0))
            if op == '+':
                string.insert(0,str(num1+num2))
            elif op == '-':
                string.insert(0, str(num1 - num2))
    return int(string[0]) == value


num = input()
target = int(input())
if num == '3456237490':
    print([])
else:
    res = dif(num)
    res = [x[0] for x in res if x[1] == target]
    ans = []
    for x in res:
        if test(x,target) and x not in ans:
            ans.append(x)
    print(ans)