def check():
    index=0
    record=[]
    maxLength=0
    while index<len(arr):
        temp=0
        for i in range(0,index):
            if arr[i]<arr[index]:
                temp=max(temp,record[i])   # !!!这个很容易直接用temp=1然后if里temp+=1就有问题
        record.append(temp+1)
        maxLength=max(maxLength,record[index])
        index+=1

    return maxLength

if __name__ == '__main__':
    arr=list(map(int,input().split(",")))
    print(check())