
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        line = input()
        for j in range(len(line)):
            res = ''
            pre = ''
            if line[j] == pre:
                continue
            else:
                res += line[j]
                pre = line[j]
        print(res)
