row = int(input())
Matrix = []
for i in range(row):
    line = list(map(int, input().split(",")))
    Matrix.append(line)
threshole = int(input())
Max = 0
for j in range(len(Matrix)):
    for k in range(len(Matrix[0])):
        length = 0
        count = 0
        while 1:
            if j + length >= len(Matrix) or k + length >= len(Matrix[0]):
                break
            else:
                for m in range(length+1):
                    count += Matrix[j][k+m]
                    count += Matrix[j+m][k]
                count -= Matrix[j+length-1][k+length-1]
                if count <= threshole:
                    length += 1
                    Max = max(Max, length)
                else:
                    break

        Max = max(Max, length)
print(Max)
