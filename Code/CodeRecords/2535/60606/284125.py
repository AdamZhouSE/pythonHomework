#如果位置和原数组一样，那么就说明可以分割
array = input()[1:-1].split(",")
array = [int(x) for x in array]
origin = array.copy()
origin.sort()
set_origin = set()
set_array = set()
count = 0
for i in range(len(array)):
    set_origin.add(origin[i])
    set_array.add(array[i])
    if len(set_origin.difference(set_array)) == 0:
        count+=1
        set_origin = set()
        set_origin.add(origin[i])
        set_array.add(array[i])
print(count)