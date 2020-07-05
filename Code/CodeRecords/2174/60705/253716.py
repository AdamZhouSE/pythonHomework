# 返回a，b两岛间的危险系数，若不存在路则返回-1
def func(matrix, a, b):
    return -1
    

if __name__ == '__main__':
        
    line1 = list(map(int, input().split(" ")))
    n = line1[0]
    q = line1[1]
    
    t = [0 for i in range(n)]
    matrix = [t for i in range(n)]
    
    for i in range(0, q):
        line = list(map(int, input().split(" ")))
        event = line[0]
        island1 = line[1]
        island2 = line[2]
    
        # 事件0：在x岛和y岛之间建成一座危险系数为v的桥
        if event == 0:
            index = line[3]
            matrix[island1][island2] = index
            matrix[island2][island1] = index
    
        # 事件1：x岛和y岛之间岛桥没了
        elif event == 1:
            matrix[island1][island2] = 0
            matrix[island2][island1] = 0
    
    
        # 事件2：询问x岛到y岛的危险系数
        else:
            print(func(matrix, island1, island2))
