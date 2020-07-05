def exchange(index):
    arrList=[startArr,endArr,profitArr]
    for arr in arrList:
        temp=arr[index]
        arr[index]=arr[index+1]
        arr[index+1]=temp
if __name__ == '__main__':
    startArr=eval(input())
    endArr=eval(input())
    profitArr=eval(input())

    for i in range(len(startArr)-1):
        for j in range(len(startArr)-i-1):
            start1=startArr[j]
            start2=startArr[j+1]
            if start1>start2:
                exchange(j)

    record=[]
    for i in range(len(startArr)):
        start=startArr[i]
        profit=profitArr[i]
        for j in range(0,i): # TODO 初始问题
            end=endArr[j]
            if end<=start and record[j]+profitArr[i]>profit:
                profit=record[j]+profitArr[i]
        record.append(profit)

    print(max(record))
