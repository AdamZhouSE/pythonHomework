def dfs(sum, num, arr, start, n):
    if num==0:
        if sum==n:
            return True
        else:
            return False
    for i in range(start,10):
        arr.append(i)
        if dfs(sum+i, num-1, arr, i+1, n):
            return True
        else:
            arr.remove(i)
        

if __name__=='__main__':
    container=eval(input())
    n=container[1]
    k=container[0]
    arr=[]
    result=[]
    for i in range(1, 9):
        if dfs(0, k, arr, i, n):
            result.append(arr.copy())
        arr.clear()
    print(result)


