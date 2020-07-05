def arrays_18_coupleNum(list = []):
    count = 0
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]*2:
                count+=1
    print(count)
if __name__ =='__main__':
    list = eval(input())
    arrays_18_coupleNum(list)