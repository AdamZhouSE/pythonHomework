def bin_seq(n):
    ans = []
    for i in range(1,n+1):
        ans.append(bin(i).replace('0b',''))
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(bin_seq(n))
    for res in ans:
        for no in res:
            print(no,end=" ")
        print()