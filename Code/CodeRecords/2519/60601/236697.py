if __name__ == '__main__':
    A = []
    line = input()
    line = line[1:len(line)-1]
    A = list(map(int,line.split(',')))
    loge = True
    A.sort(reverse=True)
    for i in range(len(A) - 2):
        if A[i + 2] + A[i + 1] > A[i]:
            print(A[i] + A[i + 1] + A[i + 2])
            loge = False
            break
    if loge:
        print(0)
