def biasSort(Matrix):
    for i in range(len(Matrix)):
        vertex = len(Matrix) - i - 1
        length = findSquare(Matrix, vertex, 0)
        k = 0
        for j in range(vertex, vertex + length):
            l = k + 1
            for m in range(j + 1, vertex + length):
                if Matrix[j][k] > Matrix[m][l]:
                    temp = Matrix[j][k]
                    Matrix[j][k] = Matrix[m][l]
                    Matrix[m][l] = temp
                l += 1
            k += 1

    for vertex in range(1, len(Matrix[0])):
        length = findSquare(Matrix, 0, vertex)
        j = 0
        for i in range(vertex, vertex + length):
            m = j + 1
            for k in range(i + 1, vertex + length):
                if Matrix[j][i] > Matrix[m][k]:
                    temp = Matrix[j][i]
                    Matrix[j][i] = Matrix[m][k]
                    Matrix[m][k] = temp
                m += 1
            j += 1
    return Matrix


def findSquare(Matrix, Vertex, width):

    result = 0
    for i in range(Vertex, len(Matrix)):
        result += 1
        if width + 1 >= len(Matrix[i]):
            break
        width += 1
    return result


string = list(input())
for i in range(len(string)):
    if string[i]==','and string[i-1]==']':
        string[i]=' '
string=''.join(string)
List=list(map(str,string.split(' ')))
Matrix=[]
for i in range(len(List)):
    List[i]=List[i].replace('[','')
    List[i]=List[i].replace(']','')
    Matrix.append(list(map(int,List[i].split(','))))
print(biasSort(Matrix))