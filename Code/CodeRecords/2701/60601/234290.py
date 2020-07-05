
def solve(moves):
    data = [[''] * 3 for _ in range(3)]
    p = 'X'

    def check(p):
        if all(data[0][i] == p for i in range(3)) or \
                all(data[1][i] == p for i in range(3)) or \
                all(data[2][i] == p for i in range(3)) or \
                all(data[i][0] == p for i in range(3)) or \
                all(data[i][1] == p for i in range(3)) or \
                all(data[i][2] == p for i in range(3)) or \
                all(data[i][i] == p for i in range(3)) or \
                all(data[i][2 - i] == p for i in range(3)):
            return True
        return False

    for i, j in moves:
        data[i][j] = p
        if check(p):
            return 'B' if p == 'O' else 'A'
        p = 'X' if p == 'O' else 'O'
    return "Draw" if len(moves) == 9 else "Pending"


if __name__ == '__main__':
    line = input()
    line = line[1:len(line) - 1]
    array = line.split(']')
    M =[]
    for i in array:
        if len(i)==0:continue
        if i[0]=='[':
            i = i[1:len(i)]
        else: i = i[2:len(i)]
        i = i.replace(',',' ')
        i = list(map(int,i.split()))
        M.append(i)
    #print(M)
    print(solve(M))