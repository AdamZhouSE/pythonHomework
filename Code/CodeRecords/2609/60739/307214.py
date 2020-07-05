def printKDistinct(arr, n, k):
    dist_count = 0
    for i in range(n):

        j = 0
        while j < n:
            if (i != j and arr[j] == arr[i]):
                break
            j += 1

        if (j == n):
            dist_count += 1

        if (dist_count == k):
            return arr[i]

    return -1

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;


n = int(input())
for i in range(n):
    t1 = getInput()
    t2 = getInput()
    print(printKDistinct(t2, t1[0], t1[1]))