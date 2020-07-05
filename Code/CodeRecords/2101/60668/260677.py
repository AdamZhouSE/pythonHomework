def nums_7_happyNum(n):
    re = []
    while n != 1:
        a = list(str(n))
        n = 0
        for item in a:
            n+= pow(int(item),2)
        re.append(n)
        if len(re) != len(set(re)):
            return False
    return True
if __name__=='__main__':
    n = int(input())
    print(nums_7_happyNum(n))