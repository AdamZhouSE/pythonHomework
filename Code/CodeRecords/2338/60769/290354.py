def check(arr,k):
    for i in arr:
        temp = arr.copy()
        temp.remove(i)
        if k-i in temp:
            return 'Yes'
    return 'No'


if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(check(arr,k))