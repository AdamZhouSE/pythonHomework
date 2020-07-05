def func(mat:list) -> int:
    MAX_ = 1
    for i in range(len(mat)-1):
        tmp = 1
        for j in range(i, len(mat)-1):
            if mat[j] < mat[j+1] :
                tmp += 1
            else:
                break
        if tmp > MAX_ :
            MAX_ = tmp
    return MAX_

n = "l = " + input()
exec(n)
print(func(l))