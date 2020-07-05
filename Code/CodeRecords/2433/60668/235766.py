def arrays_1(list):
    list = eval(list)
    list = sorted(list)
    list_all = []
    list_single = []
    n = len(list)
    i = 0
    while i<n:
        left = list[i][0]
        right = list[i][1]
        while i<n-1 and list[i+1][0]<=right:
            i = i+1
            right = max(list[i][1],right)
        list_single.append(left)
        list_single.append(right)
        list_all.append(list_single)
        list_single = []
        i = i + 1
    print(list_all)
if __name__ == '__main__':
    list = input()
    arrays_1(list)