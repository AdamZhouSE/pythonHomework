total_size = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
ope_n = int(input())
operations = []
for i in range(ope_n):
    operations.append(input())
if total_size % 2 == 1:
    mid_i = total_size // 2
else:
    mid_i = total_size // 2 - 1
# 初始中位数
mid = arr[mid_i]

# 左边的大根堆（小于等于中位数）
bhp = []


def bhp_insert(x):
    bhp.append(x)
    bhp_size = len(bhp)
    i = bhp_size - 1
    while i > 0:
        # 子大于父就交换（保证父大于等于子）
        if bhp[i] > bhp[(i - 1) // 2]:
            t = bhp[i]
            bhp[i] = bhp[(i - 1) // 2]
            bhp[(i - 1) // 2] = t
        i = (i - 1) // 2


def bhp_sort(b):
    bhp_size = len(b)
    i = bhp_size - 1
    for j in range(i, 0, -1):
        while j > 0:
            # 子大于父就交换（保证父大于等于子）
            if b[j] > b[(j - 1) // 2]:
                t = b[j]
                b[j] = b[(j - 1) // 2]
                b[(j - 1) // 2] = t
            j = (j - 1) // 2


# 初始化大根堆
for i in range(0, mid_i + 1):
    bhp_insert(arr[i])
# 右边的小根堆（大于中位数）
shp = []


def shp_insert(x):
    shp.append(x)
    shp_size = len(shp)
    i = shp_size - 1
    while i > 0:
        # 子小于父就交换（保证父小于等于子）
        if shp[i] < shp[(i - 1) // 2]:
            t = shp[i]
            shp[i] = shp[(i - 1) // 2]
            shp[(i - 1) // 2] = t
        i = (i - 1) // 2


def shp_sort(b):
    shp_size = len(b)
    i = shp_size - 1
    for j in range(i, 0, -1):
        while j > 0:
            # 子小于父就交换（保证父小于等于子）
            if b[j] < b[(j - 1) // 2]:
                t = b[j]
                b[j] = b[(j - 1) // 2]
                b[(j - 1) // 2] = t
            j = (j - 1) // 2


# 初始化小根堆
for i in range(mid_i + 1, total_size):
    shp_insert(arr[i])
for instr in operations:
    if instr == 'mid':
        print(mid)
    else:
        toadd = int(instr[4:])
        if total_size % 2 == 0:
            if toadd > mid:
                shp_insert(toadd)
                bhp_insert(shp[0])
                shp = shp[1:]
                shp_sort(shp)
                mid = bhp[0]
            else:
                bhp_insert(toadd)
                mid = bhp[0]
        else:
            if toadd > mid:
                shp_insert(toadd)
                mid = bhp[0]
            else:
                bhp_insert(toadd)
                shp_insert(bhp[0])
                # 删去bhp[0]
                bhp = bhp[1:]
                bhp_sort(bhp)
                mid = bhp[0]
        total_size += 1