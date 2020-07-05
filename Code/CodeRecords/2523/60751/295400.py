matrix=input().strip("[").strip("]").split("],[")
matrix_=[]
for i in range(len(matrix)):
    matrix_.append(list(map(int,matrix[i].split(","))))
#print(matrix_)
for i in range(len(matrix_[0])):#行
    set_=[]
    y=i
    x=0
    while(x<len(matrix_)and y<len(matrix_[0])):
        set_.append(matrix_[x][y])
        x+=1
        y+=1
    set_.sort()
    #print(set_)
    x,y,j=0,i,0
    while (x < len(matrix_) and y < len(matrix_[0])):
        matrix_[x][y]=set_[j]
        x+=1
        y+=1
        j+=1

for i in range(len(matrix_)):#列
    set_ = []
    x=i
    y=0
    while (x < len(matrix_) and y < len(matrix_[0])):
        set_.append(matrix_[x][y])
        x += 1
        y += 1
    set_.sort()
    x,y,j = i,0,0
    while (x < len(matrix_) and y < len(matrix_[0])):
        matrix_[x][y] = set_[j]
        x += 1
        y += 1
        j += 1
print(matrix_)