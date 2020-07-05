def move(num, cur_row, cur_column, row, column, step):
    ret = []
    if step % 2 == 1:
        len = column - (int)(step / 2)
    else:
        len = row - (int)(step / 2)
    lst = []
    #横着走
    if step % 2 == 1:
        #向右
        if step % 4 == 1:
            for i in range(0,len):
                lst.append(num[cur_row][cur_column + i])
            ret.append(cur_row + 1)
            ret.append(cur_column + len - 1)
        #向左
        else:
            for i in range(0,len):
                lst.append(num[cur_row][cur_column - i])
            ret.append(cur_row - 1)
            ret.append(cur_column - len + 1)
    #竖着走
    else:
        #向下
        if step % 4 == 2:
            for i in range(0,len):
                lst.append(num[cur_row + i][cur_column])
            ret.append(cur_row + len - 1)
            ret.append(cur_column - 1)
        #向上
        else:
            for i in range(0,len):
                lst.append(num[cur_row - i][cur_column])
            ret.append(cur_row - len + 1)
            ret.append(cur_column + 1)
    ret.append(lst)
    return ret

def rotate_traverse(nummat,row,column):
    step = 1
    i = j = 0
    seq = []
    while 1:
        res = move(nummat, i, j, row, column, step)
        #print(res)
        if res[2] == []:
            break
        for num in res[2]:
            seq.append(num)
        i = res[0]
        j = res[1]
        step = step + 1
    return seq


def reshape(numlst,row,column):
    nummat = []
    for i in range(0,row):
        lst = numlst[i*column:i*column+column]
        nummat.append(lst)
    return nummat

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        M,N = map(int,input().split())
        numlst = list(map(int,input().split()))
        nummat = reshape(numlst,M,N)
        #print(nummat)
        ans.append(rotate_traverse(nummat,M,N))
    for seq in ans:
        for no in seq:
            print(no,end=" ")
        print()