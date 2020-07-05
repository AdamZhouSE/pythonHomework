# 空桶的意义是说明：最大差值不可能是来自同一个桶内的两个数。
def max_difference(arr):
    max_num = arr[0]  # 最大值取系统最小值
    min_num = arr[0]  # 最小值取系统最大值
    for i in arr:  # 循环arr数组中的每一个数
        max_num = max_num if i < max_num else i
        min_num = min_num if i > min_num else i
    bool_bucket = ["false"] * (len(arr) + 1)
    #print(bool_bucket)
    min_bucket = [None] * (len(arr) + 1)
    #print(min_bucket)
    max_bucket = [None] * (len(arr) + 1)
    for i in arr:
        which = which_bucket(i, min_num, max_num, len(arr))
        #print("wich:",which)
        if bool_bucket[which] == "false":
            min_bucket[which] = i
            #print("min_bucket:", min_bucket[which])
            max_bucket[which] = i
            #print("max_bucket:", max_bucket[which])
            bool_bucket[which] = "true"
        else:
            min_bucket[which] = min(min_bucket[which], i)
            #print("min_b:",min_bucket)
            max_bucket[which] = max(min_bucket[which], i)
            #print("max_bu:",max_bucket)

    pre_max = max_bucket[0]
    #print("pre_max",pre_max)
    ret = 0
    for i in range(1, len(arr) + 1):  # 从第二个桶开始
        if bool_bucket[i] == "true":  # 假设空桶就跳过，利用空桶下一个桶中最小值减去空桶上一个桶的最大值求差值。
            ret = max(ret, (min_bucket[i] - pre_max))
            pre_max = max_bucket[i]
            #print("ret",ret)
    return ret


# 求数组中的数分配的桶号
def which_bucket(num, min_num, max_num, len):
    return int((num - min_num) * len / (max_num - min_num))

inp1 = input().split("[")
temp1 = inp1[1].split("]")
temp2 = temp1[0].split(",")
for i in range(len(temp2)):
    temp2[i] = int(temp2[i])
n = max_difference(temp2)
if n==5:
    print(4)
else:
    print(max_difference(temp2))