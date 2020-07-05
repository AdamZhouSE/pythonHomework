def find_all(n, k):
    ans = []
    if k == 1:
        ans.append([n])
    elif k == 2:
        for i in range(0, 10):
            for j in range(i+1, 10):
                if i + j == n:
                    ans.append([i, j])
    elif k == 3:
        for i in range(0, 10):
            for j in range(i+1, 10):
                for k in range(k+1, 10):
                    if i + j + k == n:
                        ans.append([i, j, k])
    elif k == 4:
        for i1 in range(0, 10):
            for i2 in range(i1+1, 10):
                for i3 in range(i2 + 1, 10):
                    for i4 in range(i3+1, 10):
                        if i1+i2+i3+i4 == n:
                            ans.append([i1, i2, i3, i4])
    return ans
    

if __name__ == '__main__':
    line = list(map(int, input().split(" ")))
    k = line[0]
    n = line[1]
    print(find_all(n ,k))
    
