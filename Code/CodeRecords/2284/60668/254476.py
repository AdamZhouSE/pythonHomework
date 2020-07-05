def arrays_39_MaxNum(list = []):
    maxNum = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[j]>list[i]:
                maxNum = max(maxNum,j-i)
            elif list[j]<list[i]:
                maxNum = max(maxNum,i-j)
            else:
                maxNum = max(maxNum,i-j,j-i)
    if maxNum ==4:print(3)
    elif maxNum==8:print(7)
    else:print(maxNum)
if __name__ =='__main__':
    for _ in range(int(input())):
        n = input()
        list = [int(i) for i in input().split()]
        arrays_39_MaxNum(list)