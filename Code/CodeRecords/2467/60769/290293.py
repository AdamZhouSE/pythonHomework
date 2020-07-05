if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        m, n, k = list(map(int, input().split()))
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        ptr1 = 0
        ptr2 = 0
        while k > 1:
            if arr1[ptr1] > arr2[ptr2]:
                ptr2 += 1
            else:
                ptr1 += 1
            k -= 1
        print(min([arr2[ptr2], arr1[ptr1]]))
