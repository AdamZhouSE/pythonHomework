def question19():
    inf = input().split()
    n = int(inf[0])
    d = int(inf[1])
    array = list(map(int, input().split()))
    step = 0
    for i in range(1,len(array)):
        while array[i] <= array[i-1]:
            array[i] += d
            step += 1
    return step
if __name__ == '__main__':
    print(question19())