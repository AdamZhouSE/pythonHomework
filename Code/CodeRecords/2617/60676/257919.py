def get_k_1s(s, k):
    
    # record the indexes of all the 1s
    index_of_1 = []
    res = 0
    for i in range(len(s)):
        if s[i] == '1':
            index_of_1.append(i)
    
    # operate every k 1s
    for i in range(len(index_of_1) - k + 1):
        left_zeros = index_of_1[i]
        if i > 0:
            left_zeros -= index_of_1[i-1] + 1
        right_zeros = len(s) - index_of_1[i+k-1] - 1
        if i < len(index_of_1) - k:
            right_zeros = index_of_1[i+k] - index_of_1[i+k-1] - 1
        res += (left_zeros + 1) * (right_zeros + 1)
    
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        a = input().split()
        result.append(get_k_1s(a[0], int(a[1])))
    for i in range(len(result)):
        print(result[i])
