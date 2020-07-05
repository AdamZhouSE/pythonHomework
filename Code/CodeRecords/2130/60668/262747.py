def nums_18_NthNum(n):
    re = ""
    for i in range(1000):
        re += str(i)
    print(re[n-1])
if __name__=='__main__':
    n = int(input())
    nums_18_NthNum(n)