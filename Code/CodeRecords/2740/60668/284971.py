def strings_12_minT(lis=[]):
    re = []
    for item in lis:
        time = int(item[0:2])*60+int(item[3:])
        if time in re:
            return 0
        re.append(time)
    re = sorted(re)
    re.append(re[0]+1440)
    mins = 1440
    for i in range(len(re)-1):
        mins = min(mins,abs(re[i+1]-re[i]))
    return mins
if __name__=='__main__':
    lis = eval(input())
    print(strings_12_minT(lis))