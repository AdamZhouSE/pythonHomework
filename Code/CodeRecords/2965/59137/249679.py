def s15():
    KM = input().split()
    K = int(KM[0])
    M = int(KM[1])
    string = input()
    N = int(input())
    for i in range(N):
        if len(string) > M:
            string = string[0:M]
        order = input().split()
        begin = int(order[0])
        length = int(order[1]) - begin
        sub = string[begin: begin+length]
        index = int(order[2])
        string = string[0: index] + sub + string[index: len(string)]
    print(string[0: K], end="")


s15()