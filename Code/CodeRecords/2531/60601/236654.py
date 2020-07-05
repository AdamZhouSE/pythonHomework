def num(s,c):
    count = 0
    for i in s:
        if c == i:
            count = count + 1
    return count

if __name__ == '__main__':
    s = input()
    dic = {}
    for i in s:
        if i not in dic.keys():
            dic[i] = num(s,i)
    #print(dic)
    s = sorted(dic.items(), key =lambda x: x[1], reverse=True)
    #print(s)
    #print(type(s[0]))
    re = ''
    for i in s:
        for j in range(i[1]):
            re = re + i[0]
    print(re)