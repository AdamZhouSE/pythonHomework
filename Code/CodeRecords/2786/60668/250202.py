def arrays_27_training(list = []):
    list = sorted(list)
    days = 1
    for i in range(len(list)):
        if days <= list[i]:
            days += 1
    print(days-1)
if __name__=='__main__':
    n = input()
    list = [int(i) for i in input().split()]
    arrays_27_training(list)
