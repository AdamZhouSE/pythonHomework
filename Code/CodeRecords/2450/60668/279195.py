if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    n = int(input())
    start = end = -1
    if n not in list:
        print("[-1, -1]")
    else:
        for i in range(len(list)):
            if list[i]==n:
                start = i
                break
        for i in range(start+1,len(list)):
            if list[i]==n:
                end = i
        if end==-1:
            end = start
        re = []
        re.append(start)
        re.append(end)
        print(re)