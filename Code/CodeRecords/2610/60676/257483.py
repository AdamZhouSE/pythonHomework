def method(arr):
    mp = []
    res = 0
    for i in range(len(arr)):
        res += 1
        if i > 0:
            j = i-1
            while j >= 0 and arr[j] not in arr[j+1:i+1]:
                if arr[j:i+1] not in mp:
                    mp.append(arr[j:i+1])
                    res += i-j+1
                j -= 1
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        a = input()
        result.append(method(input().split()))
    for i in range(len(result)):
        print(result[i])