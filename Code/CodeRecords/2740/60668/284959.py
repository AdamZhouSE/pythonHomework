def strings_12_minT(lis=[]):
    re = []
    for item in lis:
        time = int(item[0:2])*60+int(item[3:])
        re.append(time)
    re = sorted(re)
    mins = 1440
    for i in range(len(re)-1):
        mins = min(mins,abs(re[i+1]-re[i]))
    print(mins,end='')
if __name__=='__main__':
    lis = eval(input())
    strings_12_minT(lis)