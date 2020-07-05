def strings_14_forege(strings):
    re = []
    co = []
    s = ""
    for i in range(len(strings)):
        if strings[i]== '[':
            re.append(i)
        elif strings[i]==']':
            co.append(i)
    start = re[len(re)-1]  #找到最中间的那一部分 然后找数字就行了
    end = co[0]
    s = strings[start+2:end]
    count = 1
    for i in re:
        count *= int(strings[i+1])
    s = s*count
    strings = strings[:re[0]]+s
    print(strings,end='')
if __name__=='__main__':
    strings = input()
    strings_14_forege(strings)