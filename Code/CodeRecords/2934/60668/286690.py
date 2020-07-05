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
    s = strings[start+2:end] #找到要复读的字符串
    count = 1
    for i in range(len(re)-1):
        count *= int(strings[re[i]+1:re[i+1]]) #计算复读次数
    s = s*count
    strings = strings[:re[0]]+s #第一个[ 之前的字符补上去
    print(strings,end='')
if __name__=='__main__':
    strings = input()
    strings_14_forege(strings)