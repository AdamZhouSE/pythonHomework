def merge(array):
    for i in range(0, len(array)-1):
        if array[i+1][0] in range(array[i][0], array[i][1]+1):
            if array[i+1][1] in range(array[i][0], array[i][1]+1):
                array.remove(array[i+1])
                merge(array)
                break
            else:
                array[i][1]=array[i+1][1]
                array.remove(array[i+1])
                merge(array)
                break

if __name__=='__main__':
    array1 = input()[2:-2].split("],[")
    array2 = []
    interval = []
    for block in array1:
        divide = block.split(",")
        interval.clear()
        interval.append(int(divide[0]))
        interval.append(int(divide[1]))
        array2.append([interval[0], interval[1]])
    merge(array2)
    print(array2)