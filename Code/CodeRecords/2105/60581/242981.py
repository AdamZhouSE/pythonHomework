str = input()

i = 0
lst = []
while i < len(str):
    number = ''
    judge = False
    if str[i]=='-' or (str[i]>='0' and str[i]<='9'):
        judge = True
        number += str[i]
    while judge:
        if i + 1 == len(str):
            lst.append(int(number))
            break
        if str[i + 1] >= '0' and str[i + 1] <= '9':
            i += 1
            number += str[i]
        else:
            judge = False
            lst.append(int(number))
    i += 1

matrix1 = lst[0:4]
matrix2 = lst[4:8]

if matrix1[0]>matrix2[2] or matrix1[1]>matrix2[3] or matrix2[0]>matrix1[2] or matrix2[1]>matrix1[3]:
    answer = (matrix1[2]-matrix1[0])*(matrix1[3]-matrix1[1]) + (matrix2[2]-matrix2[0])*(matrix2[3]-matrix2[1])
else:
    matrix3 = []
    matrix3.append(max(matrix1[0],matrix2[0]))
    matrix3.append(max(matrix1[1],matrix2[1]))
    matrix3.append(min(matrix1[2],matrix2[2]))
    matrix3.append(min(matrix1[3],matrix2[3]))

    answer = (matrix1[2]-matrix1[0])*(matrix1[3]-matrix1[1]) + (matrix2[2]-matrix2[0])*(matrix2[3]-matrix2[1]) - (matrix3[2]-matrix3[0])*(matrix3[3]-matrix3[1])
print(answer)