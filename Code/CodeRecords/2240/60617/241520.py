def main():
    arrayA=input().split(",")
    arrayA=list(map(int, arrayA))
    arrayA.sort()
    n=len(arrayA)
    sum=0
    for num in arrayA:
        sum=sum+num
    for i in range(1,int(n/2)+1):
        if sum*i%n==0 and dfs(arrayA, 0, i, sum*i/n):
            print(True)
            exit()
    print(False)
def dfs(Array, begin, n, target):
    if n==0:
        return target==0
    if target<n*Array[begin]:
        return False
    for i in range(begin, len(Array)-n):
        if dfs(Array, begin+1, n-1, target-Array[i]):
            return True
    return False

if __name__ == '__main__':
    main()