import re
up=input()
arr1=input()
arr2=input()
arr3=input()
arr4=input()
arr1=arr1[3:-2]
arr2=arr2[3:-2]
arr3=arr3[3:-2]
arr4=arr4[3:-1]
arr1=re.findall(r'[\d]',arr1)
arr2=re.findall(r'[\d]',arr2)
arr3=re.findall(r'[\d]',arr3)
arr4=re.findall(r'[\d]',arr4)
new1=[]
new2=[]
new3=[]
new4=[]
for i in arr1:
    new1.append(i)
for i in arr2:
    new2.append(i)
for i in arr3:
    new3.append(i)
for i in arr4:
    new4.append(i)
down=input()
matrix=[]
matrix.append(new1)
matrix.append(new2)
matrix.append(new3)
matrix.append(new4)
m = len(matrix)
n = 0
if m > 0:
    n = len(matrix[0])
max_height = [0 for i in range(0, n)]
max_right = [n - 1 for i in range(0, n)]
max_left = [0 for i in range(0, n)]
max_area = 0

for i in range(0, m):
    left_border = 0
    right_border = n - 1

    for j in range(0, n):
        if matrix[i][j] == '1':
            max_height[j] = max_height[j] + 1
            max_left[j] = max(max_left[j], left_border)
        else:
            max_height[j] = 0
            left_border = j + 1
            max_left[j] = 0

    j = n - 1
    while j >= 0:
        if matrix[i][j] == '1':
            max_right[j] = min(max_right[j], right_border)
        else:
            right_border = j - 1
            max_right[j] = n - 1
        j = j - 1

    for j in range(0, n):
        if (max_right[j] - max_left[j] + 1) * max_height[j] > max_area:
            max_area = (max_right[j] - max_left[j] + 1) * max_height[j]
print(max_area)