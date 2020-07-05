def method(array, num):
    array.sort()
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == num:
                return 'Yes'
    return 'No'


result = []
for i in range(int(input())):
    line1 = input().split(' ')
    line2 = input().split(' ')
    for j in range(len(line2)):
        line2[j] = int(line2[j])
    result.append(method(line2, int(line1[1])))
for i in range(len(result)):
    print(result[i])