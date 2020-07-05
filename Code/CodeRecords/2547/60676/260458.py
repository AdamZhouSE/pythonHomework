def get_pairs(arr, num):
    res = 0
    record = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i] - arr[j] == num or arr[i] - arr[j] == -num) and arr[i] not in record:
                res += 1
                record.append(arr[i])
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        t = input()
        a = input().split()
        for j in range(int(t)):
            a[j] = int(a[j])
        k = int(input())
        result.append(get_pairs(a, k))
    for i in range(len(result)):
        print(result[i])