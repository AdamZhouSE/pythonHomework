def num_tree(n):
    if n < 2:
        return 1
    num = [0 for i in range(n+1)]
    num[0] = 1
    for i in range(1, n+1):
        for j in range(1,i+1):
            num[i] += num[j-1] * num[i-j]
    return num[n] % 1000000007


if __name__ == '__main__':
    print(num_tree(int(input())))