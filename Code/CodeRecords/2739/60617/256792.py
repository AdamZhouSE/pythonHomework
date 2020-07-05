def dfs(sum, num, arr, start, n, result):
    if num==0:
        if sum==n:
            result.append(arr.copy())
            return True
        else:
            return False
    for i in range(start,10):
        arr.append(i)
        if dfs(sum+i, num-1, arr, i+1, n, result):
            arr.remove(i)
        else:
            arr.remove(i)
        

if __name__=='__main__':
    container=eval(input())
    n=container[1]
    k=container[0]
    arr=[]
    result=[]
    for i in range(1, 9):
        dfs(0, k, arr, i, n, result)

    print(result)





