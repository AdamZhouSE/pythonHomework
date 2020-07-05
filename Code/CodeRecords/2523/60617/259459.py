def diagonalSort():
    matrice=eval(input())
    for i in range(0, len(matrice[0])):
        row=0
        temp=[]
        for j in range(i, len(matrice[0])):
            if row>=len(matrice):
                break
            temp.append(matrice[row][j])
            row+=1
        temp.sort()
        row=0
        for j in range(i, len(matrice[0])):
            if row>=len(matrice):
                break
            matrice[row][j]=temp[j-i]
            row+=1
    for i in range(1, len(matrice)):
        column=0
        temp=[]
        for j in range(i, len(matrice)):
            if column>=len(matrice[0]):
                break
            temp.append(matrice[j][column])
            column+=1
        temp.sort()
        column=0
        for j in range(i, len(matrice)):
            if column>=len(matrice):
                break
            matrice[j][column]=temp[j-i]
            column+=1
    print(matrice)

if __name__=='__main__':
    diagonalSort()