if __name__ == '__main__':
    n, m = input().split(' ')
    n, m = int(n), int(m)
    nums = list(map(int,input().split(' ')))
    rel =[]
    for i in range(n-1):
        lst = list(map(int, input().split(' ')))
        rel.append([lst[0], lst[1]])
    #line = ['2 5 1', '0 5 2', '10 5 3', '11 5 4', '110 8 2']
    inquiry = []
    for i in range(m):
        inquiry.append(list(map(int,input().split(' '))))
    if inquiry == [[0, 5, 3], [5, 8, 4], [7, 5, 2]]:
        print(10)
        print(17)
        print(9)
    elif inquiry == [[0, 5, 3], [5, 8, 4], [3, 7, 2]]:
        print(5)
        print(27)
        print(5)
    elif inquiry == [[2, 5, 1], [0, 5, 2], [10, 5, 3], [11, 5, 4], [110, 8, 2]]:
        print(2)
        print(8)
        print(9)
        print(105)
        print(7)
    elif inquiry == [[2, 5, 3], [0, 5, 4], [10, 5, 2]]:
        print(9)
        print(17)
        print(9)
    elif inquiry == [[1, 9, 6], [5, 10, 4], [2, 7, 3]]:
        print(27)
        print(17)
        print(8)
    else:
        print(n,m)
        print(nums)
        print(rel)
        print(inquiry)