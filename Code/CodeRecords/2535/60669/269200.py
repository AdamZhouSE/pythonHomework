def check(index):
    for j in range(0, index + 1):
        if arr[j]>index:
            return False
    for j in range(index+1,len(arr)):
        if arr[j]<=index:
            return False
    return True
        


if __name__ == '__main__':
    arr = eval(input())
    dict = {}
    for i in range(0, len(arr)):
        dict[arr[i]] = i
    arr.sort
    result = 0
    for i in range(0, len(arr)):
         temp=check(i)
         if temp:
             result+=1
    print(result)
