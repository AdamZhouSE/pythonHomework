import re
inp = re.split(r"[\[\],]", input())
data = []
for c in inp:
    # 因为要求未出现的最小正整数，所以在这里就删除负数
    if c != "" and int(c) > 0:
        data.append(int(c))
data.sort()
# 如果全是负数，那么数组为空，最小正整数为1
if len(data) == 0:
    print(1)
else:
    # 如果数组中首位大于1，那么未出现的最小正整数就是1
    if data[0] > 1:
        print(1)
    else:
        # 假设最小正整数为数组首位+1
        min_int = data[0]+1
        hasPrint = False
        for i in range(1, len(data)):
            # 如果后一位不是前一位加1，那么直接得到最小正整数
            if data[i] != min_int:
                print(min_int)
                hasPrint = True
                break
            else:
                min_int = data[i]+1
        if not hasPrint:
            print(min_int)
