def arrays_45_gap(list=[]):
    maxG = 0
    for i in range(len(list)-1):
        if list[i+1]-list[i]>maxG:
            maxG = list[i+1] - list[i]
    if maxG==0:
        print(-1)
    else:
        print(maxG)
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        list = [int(i) for i in input().split()]
        arrays_45_gap(list)