def find_moun(start, end):
    middle = int((start+end)/2)
    if start == end:
        if numbers[start-1] < numbers[start] and numbers[start+1] < numbers[start]:
            return start
        else:
            return -1
    elif start == end - 1:
        if numbers[start-1] < numbers[start] and numbers[start+1] < numbers[start]:
            return start
        elif numbers[end-1] < numbers[end] and numbers[end] > numbers[end+1]:
            return end
        else:
            return -1
    ind = find_moun(start, middle)
    if ind != -1:
        return ind
    elif numbers[middle-1] < numbers[middle] and numbers[middle] > numbers[middle + 1]:
        return middle
    elif find_moun(middle, end) != -1:
        return find_moun(middle, end)
    else:
        return -1


num = input().split(",")
numbers = [int(i) for i in num]
numbers.insert(0, -9)
numbers.append(-9)
index = find_moun(1, len(numbers)-2)
print(index - 1)
