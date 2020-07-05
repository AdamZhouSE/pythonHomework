def arrays_39_MaxNum(list = []):
    maxNum = 0
    for i in range(len(list)):
        for j in range(i,len(list)):
            if list[j]>=list[i]:
                maxNum = max(maxNum,j-i)
    print(maxNum)
if __name__ =='__main__':
    for _ in range(int(input())):
        n = input()
        list = [int(i) for i in input().split()]
        arrays_39_MaxNum(list)