def check(index):
    for j in range(0, index + 1):
        if dict[arr[j]]>index:
            return False
    for j in range(index+1,len(arr)):   
        if dict[arr[j]]<=index:
            return False
    return True



if __name__ == '__main__':
    arr = eval(input())
    dict = {}
    for i in range(0, len(arr)):
        dict[arr[i]] = i
    arr.sort()
    result = 1
    for i in range(0, len(arr)-1):     # 最后一个不用检查 后面没有了 而且result初始值就是1
         temp=check(i)
         if temp:
             result+=1
    print(result)
