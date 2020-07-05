def Test():
    #whoaasdsafjvnmdsfhsahfdsjgsJNvb     snmndfvhkfbhjskjvdsjvbmsdbv 3
    A=input()
    B=input()
    k=int(input())
    f=[([0]*100) for i in range(100)]
    for i in range(1,len(A)+1):
        f[i][0]=i*k
    for i in range(1,len(B)+1):
        f[0][i]=i*k
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            f[i][j] = min(f[i][j - 1] + k, f[i - 1][j] + k)
            f[i][j] = min(f[i][j], f[i - 1][j - 1] + abs(ord(A[i - 1]) - ord(B[j - 1])))
    print(f[len(A)][len(B)],end="")

if __name__ == "__main__":
    Test()