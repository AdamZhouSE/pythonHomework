def check():
    for i in range(1,int(size/2)+1):
        goal=i*averageB
        index=-1
        for k in range(0,size-1):
            if arr[k]<=goal/2 and goal/2<=arr[k+1]:    # 若两个数加起来是goal 这两个数必在goal/2的两侧
                index=k
                break
        for diff in range(0,min(index,size-index)):   # 看左右两边哪个小
            left=arr[index]
            right=arr[index+1]
            if left+right==goal:
                return True
    return False


if __name__ == '__main__':
    arr = list(map(int, input().split(",")))
    arr.sort()
    size = len(arr)
    average = 0
    for item in arr:
        average += item
    average /= size
    # B和C的要乘2
    averageB = average * 2
    print(check())
