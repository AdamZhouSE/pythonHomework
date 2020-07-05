if __name__ == '__main__':
    t = input().split()
    arr = [i+1 for i in range(int(t[0]))]
    for i in range(int(t[1])):
        tmp = input().split()
        ptr1 = int(tmp[0]) - 1
        ptr2 = int(tmp[1]) - 1
        while ptr1 < ptr2:
            arr[ptr1] = arr[ptr1] + arr[ptr2]
            arr[ptr2] = arr[ptr1] - arr[ptr2]
            arr[ptr1] = arr[ptr1] - arr[ptr2]
            ptr1 += 1
            ptr2 -= 1
    for i in range(len(arr)):
        print(arr[i], end=' ')