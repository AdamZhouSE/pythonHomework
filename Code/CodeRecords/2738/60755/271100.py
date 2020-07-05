def judge(matrix,m,n,i,k):
    for a in range(i):
        for b in range(k):
            if matrix[m+a][n+b]!="1":
                return False
    return True


def solve(matrix,res):
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            for m in range(i+1):
                for n in range(k+1):
                    if judge(matrix,m,n,len(matrix)-i,len(matrix[0])-k):
                        res.append((len(matrix)-i)*(len(matrix[0])-k))
    return res


input()
matrix = []
while True:
    s = input()
    if s == "]":
        break
    else:
        string = ""
        for i in s:
            if i.isdecimal():
                string = string + i + " "
        matrix.append(string.split(" ")[:-1])
res = solve(matrix,[])
print(max(res))
    