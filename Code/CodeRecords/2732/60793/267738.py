for test in range(0, int(input())):
    temp_ls = list(map(int, input().split()))
    print(pow(temp_ls[0], temp_ls[1]) % temp_ls[-1])