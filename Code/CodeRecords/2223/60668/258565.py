def nums_4_Wrong(list=[]):
    re = []
    re_0 = sorted(list)
    co = 0
    co_0 = []
    for i in range(len(list)-1):
        if re_0[i]==re_0[i+1]:
            co = re_0[i]
    for i in range(len(list)):
        if list[i]==co:
            co_0.append(i)
    re.append(list[co_0[0]-1])
    re.append(list[co_0[0]])
    print(re)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_4_Wrong(list)