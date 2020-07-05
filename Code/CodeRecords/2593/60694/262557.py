def findPairs(arr, n):
    Hash = {}
    ans = []
    for i in range(n-1):
        for j in range(i+1, n):
            sum = arr[i] + arr[j]
            if sum in Hash.keys():
                # print previous pair and current
                prev = Hash.get(sum)
                ans.append([prev[0], prev[1], i, j])

            else:
                Hash[sum] = [i, j]
    if ans:
        ans.sort()
        print(" ".join(map(str, ans[0])))
    else:
        print("no pairs")


T = int(input())
for _ in range(T):
    N = int(input())
    exp = input()
    if "," in exp:
        A = list(map(int, exp.split(", ")))
    else:
        A = list(map(int, exp.split()))
    findPairs(A, N)

