import ast
def solve(section):
    if len(section) <= 1:
        return section
    section = sorted(section, key=lambda x: x[0])
    s = section[0][0]
    e = section[0][1]
    res = []
    for i in range(1,len(section)):
        if section[i][0] > e:
            res.append([s, e])
            s = section[i][0]
            e = section[i][1]
        else:
            e = max(e,section[i][1])
    res.append([s, e])
    return res


str_list = input()
new_str = ast.literal_eval(str_list)
data = input()
new_data = ast.literal_eval(data)
new_str.append(new_data)
print(solve(new_str))