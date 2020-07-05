def rearrange(arr):
    odd_list = []
    even_list = []
    for i in range(len(arr)):
        if int(arr[i]) % 2 == 0:
            even_list.append(arr[i])
        else:
            odd_list.append(arr[i])
    return even_list + odd_list


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        a = input()
        result.append(rearrange(input().split()))
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end=' ')
        print()