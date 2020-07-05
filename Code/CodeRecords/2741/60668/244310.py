def arrays_16_longest(list = []):
    maxLength = 0
    maxNum = 0
    for i in range(0,len(list)-1):
        if list[i+1]>list[i]:
            maxNum +=1
        else:
            maxNum = 0
        if maxNum>maxLength:
            maxLength = maxNum
    print(maxLength+1)
if __name__ =='__main__':
    list = eval(input())
    arrays_16_longest(list)