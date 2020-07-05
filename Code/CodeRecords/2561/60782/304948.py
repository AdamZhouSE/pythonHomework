def main(mat1,mat2):
    return [[sum(mat1[i][s]*mat2[s][j] for s in range(len(mat1[0]))) for j in range(len(mat2[0]))] for i in range(len(mat1))] 
print(main(eval(input()),eval(input())))

