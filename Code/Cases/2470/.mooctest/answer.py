#code
def rotmat90clock(m,n):
    for i in range(n//2):
        for j in range(i,n-i-1):
            temp = m[i][j]
            m[i][j] = m[n-j-1][i]
            m[n-j-1][i] = m[n-i-1][n-j-1]
            m[n-i-1][n-j-1] = m[j][n-i-1]
            m[j][n-i-1] = temp
    return m

if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        size = int(input())
        list1 = list(int(x) for x in input().split())
        new = []
        matrix = []
        n = 0
        for i in range(size):
            for j in range(size):
                new.append(list1[n])
                n = n+1
            matrix.append(new)
            new = []
        out = rotmat90clock(matrix,size)
        list1 = ''
        for i in range(len(out)):
            for j in range(len(out)):
                list1=list1+str(out[i][j])+" "
        print(list1)