def password_lock():
    n=int(input())
    arr_angle=[]
    for i in range(0, n):
        arr_angle.append(int(input()))
    if dfs(arr_angle, n, 0, 0) or dfs(arr_angle, n, 0, 1):
        print("YES")
    else:
        print("NO")

def dfs(arr, times, angle, direction):
    if angle%360==0:
        angle=0
    if times==0:
        if angle==0:
            return True
        else:
            return False
    if direction==0:
        angle+=arr[len(arr)-times]
        times-=1
    else:
        angle-=arr[len(arr)-times]
        times-=1
    if dfs(arr, times, angle, 0) or dfs(arr, times, angle, 1):
        return True
    else:
        return False

if __name__=='__main__':
    password_lock()