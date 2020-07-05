def arrays_34_leastFlat(arr,plat_num,last_time,lis):
    if min(lis) ==1:
        print(plat_num)
        return
    for i in range(len(arr)):
        if lis[i]==1:
            continue
        if arr[i][0]>=last_time:
            last_time = arr[i][1]
            lis[i] = 1
    if min(lis) ==1:
        print(plat_num)
        return
    else:
        arrays_34_leastFlat(arr,plat_num+1,0,lis)
def takeSecond(ele):
    return ele[1]
if __name__=='__main__':
    for _ in range(int(input())):
        n = int(input())
        list_arr = [int(i) for i in input().split()]
        list_leav = [int(i) for i in input().split()]
        arr = []
        for i in range(n):
            arr.append([list_arr[i],list_leav[i]])
        arr.sort(key=takeSecond)
        lis = [0]*n
        arrays_34_leastFlat(arr,1,0,lis)