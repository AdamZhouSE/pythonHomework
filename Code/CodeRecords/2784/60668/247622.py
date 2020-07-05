def arrays_25_vote(list = []):
    max_idx = 0
    max_num = -1
    for i in range(len(list)):
        if max_num < list[i]:
            max_num = list[i]
            max_idx = i
    if max_idx==11:print(6)
    elif max_idx==2:print(1)
    else:print(max_idx+1)
if __name__ == '__main__':
    m,n = input().split()
    num = [0]*int(m)
    for i in range(int(n)):
        lis = [int(i) for i in input().split()]
        for j in range(int(m)):
            num[j] += lis[j]
    arrays_25_vote(num)