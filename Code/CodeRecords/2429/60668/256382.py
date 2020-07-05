def arrays_45_gap(list=[]):
    maxG = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[j]-list[i]>maxG:
                maxG = list[j] - list[i]
    if maxG==0:
        print(-1)
    else:
        print(maxG)
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        list = [int(i) for i in input().split()]
        arrays_45_gap(list)