def arrays_32_count(list = []):
    list_re = []
    co = 0
    for i in range(0,len(list)):
        if list[i]==1:
            co+=1
            list_re.append(list[i-1])
    print(co)
    for i in range(len(list_re)-1,0,-1):
        print(list_re[i],end = ' ')
    print(list_re[0])
if __name__ =='__main__':
    n =input()
    list = [int(i) for i in input().split()]
    arrays_32_count(list)