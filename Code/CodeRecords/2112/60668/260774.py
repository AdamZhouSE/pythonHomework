def nums_11_notIN(list = []):
    co = 0
    for i in range(0,len(list)+1):
        if i not in list:
            co = i
    print(co)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_11_notIN(list)