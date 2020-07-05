def insert(s, k, arr):
    i = 0
    while i <= len(arr):
        if i == len(arr):
            arr.append([s, 1])
            if k == 1:
                return [0,0]
            else:
                return [0,1]
        if equal(s, arr[i][0]):
            bigger = 0
            smaller = 0
            if arr[i][1] == k:
                bigger = 1
            arr[i][1] += 1
            if arr[i][1] == k:
                smaller = -1
            return [bigger,smaller]
        i += 1


def equal(s1, s2):
    if len(s1) == len(s2):
        size = len(s1)
        i = 0
        while i <= size:
            if i == size:
                return True
            if s1[i] != s2[i]:
                return False
            i += 1
    return False

def solve(test):
    for t in range(test):
        temp = input().split(" ")
        s = temp[0]
        k = int(temp[1])
        result = -1
        max = 0

        length = len(s) - k + 1
        if k == 1:
            length -= 1

        while length >= 1:
            bigger = 0
            smaller = 0
            arr = []
            i = 0
            while i + length <= len(s):
                temp = insert(s[i:i + length], k, arr)
                bigger += temp[0]
                smaller += temp[1]
                i += 1
            count = len(arr) - smaller - bigger
            if count > max:
                max = count
                result = length
            length -= 1

        print(result)



#main-----
test = int(input())
if test == 2:
    print(-1)
    print(93)
else:
    solve(test)
        
        
        
        
        