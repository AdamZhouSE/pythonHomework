def local_sort(arr, opr):
    sld = arr[int(opr[1])-1:int(opr[2])]
    sld.sort()
    if opr[0] == '1':
        sld.reverse()
    return arr[:int(opr[1])-1] + sld + arr[int(opr[2]):]


if __name__ == '__main__':
    tms = int(input().split()[1])
    nums = input().split()
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    for i in range(tms):
        nums = local_sort(nums, input().split())
    q = eval(input())
    print(nums[q-1])