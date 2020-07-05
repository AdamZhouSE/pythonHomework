if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    co = []
    for i in range(len(list)):
        re = 1
        for j in range(i,len(list)):
            if list[j]>list[i]:
                re+=1            
        co.append(re)
    print(max(co))