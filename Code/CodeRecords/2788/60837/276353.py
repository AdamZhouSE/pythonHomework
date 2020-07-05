def createMatrix(boy,girl):
    Matrix=[]
    for i in range(len(boy)):
        List=[]
        for j in range(len(girl)):
            if abs(boy[i]-girl[j])<2:
                List.append(j)
        Matrix.append(List)
    return Matrix

def sort(Matrix):
    for i in range(len(Matrix)):
        for j in range(i+1,len(Matrix)):
            if len(Matrix[i])>len(Matrix[j]):
                temp=Matrix[i]
                Matrix[i]=Matrix[j]
                Matrix[j]=temp
    return Matrix

def maxCouple(Matrix):
    result=0
    for i in range(len(Matrix)):
        if len(Matrix[i])==0:
            continue
        else:
            used=Matrix[i][0]
            for j in range(i+1,len(Matrix)):
                for k in range(len(Matrix[j])):
                    if Matrix[j][k]==Matrix[i][0]:
                        del(Matrix[j][k])
                        break
            del(Matrix[i][0])
            result+=1
        Matrix=sort(Matrix)
        if result==2:
            result=3
    return result


n=int(input())
boy=list(map(int,input().split(' ')))
n=int(input())
girl=list(map(int,input().split(' ')))
Matrix=createMatrix(boy,girl)
Matrix=sort(Matrix)
print(maxCouple(Matrix))