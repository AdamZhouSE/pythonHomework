def water_volume(arr_list):
    """
    返回积水量
    :param arr_list: 台阶数组
    :return: 返回积水量
    """
    arr_length = len(arr_list)  # 数组的长度
    arr_left_pos = 0  # 从左开始遍历的指针的下标
    arr_right_pos = arr_length - 1  # 从右开始遍历的指针的下标
    arr_max_left = arr_list[arr_left_pos]  # 从左开始遍历的过程中的极大值
    arr_max_right = arr_list[arr_right_pos]  # 从右开始遍历的过程中的极大值
    volumes = 0  # 保存容积的变量
    while arr_left_pos < arr_right_pos:
        if arr_max_left < arr_max_right:
            arr_left_pos += 1
            if arr_list[arr_left_pos] >= arr_max_left:
                arr_max_left = arr_list[arr_left_pos]
            else:
                volumes += (arr_max_left - arr_list[arr_left_pos])
        else:
            arr_right_pos -= 1
            # tmp_right = arr_list[arr_right_pos]
            if arr_list[arr_right_pos] >= arr_max_right:
                arr_max_right = arr_list[arr_right_pos]
            else:
                volumes += (arr_max_right - arr_list[arr_right_pos])
    return volumes

a=eval(input())
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    #原理：高矮高就是一个容器 新建一个列表 储存高的index
    res=water_volume(list1)
    print(res)