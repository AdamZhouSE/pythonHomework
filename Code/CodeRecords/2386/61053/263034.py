def find_four_sum(numlst,tar):
    if len(numlst) < 4:
        return 0
    i = 0
    j = 1
    ans = 0
    for i in range(0,len(numlst)-3):
        for j in range(i+1,len(numlst)-2):
            k = j + 1
            h = len(numlst) - 1
            while k < h:
                cur_sum = numlst[i] + numlst[j] + numlst[k] + numlst[h]
                if cur_sum < tar:
                    k = k + 1
                elif cur_sum > tar:
                    h = h - 1
                else:
                    ans = ans + 1
                    k = k + 1
                    h = h - 1
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        numlst = list(map(int,input().split()))
        tar = int(input())
        ans.append(find_four_sum(numlst,tar))
    for no in ans:
        if no != 0:
            print(1)
        else:
            print(0)