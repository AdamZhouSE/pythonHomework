
def findLongestConseqSubseq(arr, n):
    s = set()
    ans = 0

    for ele in arr:
        s.add(ele)

    for i in range(n):
        if (arr[i] - 1) not in s:
            j = arr[i]
            while (j in s):
                j += 1

            ans = max(ans, j - arr[i])
    return ans

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    k = int(input())
    l = getInput()
    print(findLongestConseqSubseq(l, k))