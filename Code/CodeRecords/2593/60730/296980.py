num = int(input())
for k in range(num):
    length = int(input())
    mm = input()
    if "," not in mm:
        m = list(map(int, mm.rstrip().split(" ")))      # 末尾有空格
    else:
        m = list(map(int, mm.split(",")))
    Hash = {}
    ans = {}
    # Traverse through all possible pairs of arr[]
    for i in range(length - 1):
        for j in range(i + 1, length):
            sum_num = m[i] + m[j]
            if sum_num in Hash.keys() and sum_num not in ans.keys():
                prev = Hash.get(sum_num)
                ans[sum_num] = [prev[0], prev[1], i, j]
            else:
                Hash[sum_num] = (i, j)
    if ans == {}:
        print("no pairs")
    else:
        min = []
        temp = []
        if len(ans) == 1:
            for l in ans.keys():
                temp.append(ans[l][0])         # 添加数组就有双括号
                temp.append(ans[l][1])
                temp.append(ans[l][2])
                temp.append(ans[l][3])
            print(" ".join(map(str, temp)))
        else:
            for l in ans.keys():
                temp.append(ans[l])
            for i in range(len(temp) - 1):
                for j in range(i + 1, len(temp)):
                    if temp[i][0] > temp[j][0]:
                        min = temp[j]
                    elif temp[i][0] < temp[j][0]:
                        min = temp[i]
                    else:
                        if temp[i][1] > temp[j][1]:
                            min = temp[j]
                        elif temp[i][1] < temp[j][1]:
                            min = temp[i]
            print(" ".join(map(str, min)))
