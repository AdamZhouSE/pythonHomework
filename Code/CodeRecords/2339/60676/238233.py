def reverse_count(array):
    count = 0
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                count += 1
    return count


result = []
for i in range(int(input())):
    line1 = input()
    line2 = input().split(' ')
    for j in range(len(line2)):
        line2[j] = int(line2[j])
    result.append(reverse_count(line2))
for i in range(len(result)):
    print(result[i])