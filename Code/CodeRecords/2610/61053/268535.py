def all_diff(numlst):
    lst = []
    for no in numlst:
        if no in lst:
            return False
        else:
            lst.append(no)
    return True

def cal_distinct(numlst):
    ans = 0
    for i in range(len(numlst)):
        for j in range(i+1,len(numlst)+1):
            if all_diff(numlst[i:j]):
                ans += (j-i)
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        numlst = list(map(int,input().split()))
        ans.append(cal_distinct(numlst))
    for res in ans:
        print(res)