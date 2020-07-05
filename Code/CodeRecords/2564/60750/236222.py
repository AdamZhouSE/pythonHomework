import ast


def find(list_data, k, x):
    if k == len(list_data):
        return list_data
    temp = []
    for i in range(0,len(list_data)):
        differValue = abs(list_data[i] - x)
        temp.append(differValue)
    minindex = -1
    mindiffer = 0
    if temp[0] >= temp[len(temp) - 1]:
        mindiffer = temp[0]
        minindex = 0
    else:
        mindiffer = temp[len(temp) - 1]
        minindex = len(temp) - 1
    for i in range(0, len(list_data)):
        if temp[i] < mindiffer:
            mindiffer = temp[i]
            minindex = i
    if minindex == 0:
        return list_data[0:k]
    if minindex == len(temp) - 1:
        return list_data[len(temp) - k:len(temp)]
    left = minindex
    right = minindex
    for i in range(0,k - 1):
        if temp[left - 1] <= temp[right + 1]:
            left = left - 1
        else:
            right = right + 1
    return list_data[left:right+ 1]


data = input()
data_new = ast.literal_eval(data)
k1 = int(input())
x1 = int(input())
print(find(data_new,k1,x1))
