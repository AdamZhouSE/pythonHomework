if __name__ == '__main__':
    n = int(input())
    phase = []
    for _ in range(n):
        temp = input().split(' ', 1)
        phase.append(temp[1].split(' '))
    m = int(input())
    res = []
    for _ in range(m):
        ans = []
        word = input()
        for i in range(n):
            for j in phase[i]:
                if word == j:
                    ans.append(i+1)
                    break
        res.append(ans)
    for i in res:
        for j in range(len(i)-1):
            print('{0} '.format(i[j]), end='')
        print(i[len(i)-1])