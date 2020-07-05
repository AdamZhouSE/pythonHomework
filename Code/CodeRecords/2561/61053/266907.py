def find_pair(mat1,mat2,tar,size):
    count = 0
    for i in range(size**2):
        for j in range(size**2):
            if mat1[i] + mat2[j] == tar:
                count += 1
    return count

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        size,tar = map(int,input().split())
        mat1 = []
        for j in range(size):
            mat1.extend(list(map(int,input().split())))
        mat2 = []
        for j in range(size):
            mat2.extend(list(map(int,input().split())))
        ans.append(find_pair(mat1,mat2,tar,size))
    for res in ans:
        print(res)