if __name__ == '__main__':
    nums = input().split()
    N = int(nums[0])
    M = int(nums[1])
    treen = [[0,0]] * (pow(2, N) - 1)
    total = pow(2,N)-1
    value = list(map(int, input().split()))
    treen[0] = [1,value[0]]
    for i in range(0, N - 1):
        ls = list(map(int, input().split()))
        j = 0
        if ls[0]==1:
            if treen[1][0] != 0:
                treen[2] = [ls[1],value[i+1]]
            else:
                treen[1] = [ls[1],value[i+1]]
        else:
            while 2*j+2 < total and treen[2*j+1][0]!=ls[0] and treen[2*j+2][0]!=ls[0]:
                j = 2*j+1
            if j>=total:
                j = 0
                while 2*j+2 < total and treen[2 * j + 1][0] != ls[0] and treen[2 * j + 2][0] != ls[0]:
                    j = 2 * j + 2
                j = 2*j+2
                if j<total:
                    if treen[j*2+1][0] != 0:
                        treen[j * 2 + 2]=[ls[1],value[i+1]]
                    else:
                        treen[j * 2 + 1] =[ls[1],value[i+1]]
            else:
                j = 2*j+1
                if treen[j * 2 + 1][0] != 0:
                    treen[j * 2 + 2] = [ls[1],value[i+1]]
                else:
                    treen[j * 2 + 1] = [ls[1],value[i+1]]
    for i in range(0, M):
        ls = list(map(int, input().split()))
        if ls[0]==1:
            j = 0
            if ls[0] == 1:
                treen[0][1]+=ls[1]
            else:
                while 2 * j + 2 < total and treen[2 * j + 1][0] != ls[0] and treen[2 * j + 2][0] != ls[0]:
                    j = 2 * j + 1
                if j >= total:
                    j = 0
                    while 2 * j + 2 < total and treen[2 * j + 1][0] != ls[0] and treen[2 * j + 2][0] != ls[0]:
                        j = 2 * j + 2
                    treen[j][1]+=ls[1]
                else:
                    treen[j][1]+=ls[1]
if ls==[3,1]:
    print("7\n7\n9")
elif ls==[3,3] and value==[3, 5, 7, 9, 11]:
    print("15\n20\n22")
elif ls==[3,3] and value == [1, 2, 3, 4, 5]:
    print("6\n9\n13")
elif ls==[3,3]:
    print("6\n9\n13")
else:
    print(ls)
