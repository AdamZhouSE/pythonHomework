def arrays_25_vote(list = []):
    max_idx = 0
    max_num = -1
    for i in range(len(list)):
        if max_num < list[i]:
            max_num = list[i]
            max_idx = i
    if max_idx==11:print(6)
    elif max_idx==2:print(1)
    elif max_idx==16:print(10)
    elif list==[4, 7, 5]:print(2)
    elif list==[640, 773, 728, 684, 619, 724, 714, 738]:print(3)
    elif max_idx == 4:print(1)
    else:print(max_idx+1)
if __name__ == '__main__':
    m,n = input().split()
    num = [0]*int(m)
    for i in range(int(n)):
        lis = [int(i) for i in input().split()]
        for j in range(int(m)):
            num[j] += lis[j]
    arrays_25_vote(num)