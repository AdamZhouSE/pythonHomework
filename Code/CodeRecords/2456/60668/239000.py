def arrays_7_lowerNum(list = []):
    count = []
    for i in range(0,len(list)):
        co = 0
        for j in range(i,len(list)):
            if list[i]>list[j]:
                co+=1
        count.append(co)
    print(count)
if __name__ =='__main__':
    list = eval(input())
    arrays_7_lowerNum(list)