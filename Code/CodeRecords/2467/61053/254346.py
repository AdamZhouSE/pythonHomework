def find_k(A,B,k):
    i = 0
    j = 0
    ans = 0
    while i + j < k and i != len(A) and j != len(B):
        if A[i] <= B[j]:
            ans = A[i]
            i = i + 1
        else:
            ans = B[j]
            j = j + 1
    if i + j == k:
        return ans
    elif i == len(A):
        return B[k-len(A)-1]
    else:
        return A[k-len(B)-1]

if __name__ == "__main__":
    testNo = int(input())
    ans = []
    for i in range(0,testNo):
        line = input()
        m,n,k = map(int,line.split())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        ans.append(find_k(A,B,k))
    for no in ans:
        print(no)