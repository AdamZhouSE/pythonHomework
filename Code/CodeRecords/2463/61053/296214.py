def findSum(numlst,tar):
    i = 0
    j = len(numlst) - 1
    while i < j:
        temp = numlst[i] + numlst[j]
        if temp < tar:
            i += 1
        elif temp > tar:
            j -= 1
        else:
            lst = [i+1,j+1]
            return lst

if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    tar = int(input())
    res = findSum(numlst,tar)
    print(res)