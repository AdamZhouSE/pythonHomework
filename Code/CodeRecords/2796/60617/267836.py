def find_maxNotcompleteSquare():
    n=int(input())
    arr=list(map(int, input().split(" ")))
    maxNum=0
    for num in arr:
        if not isCompleteSquare(num):
            maxNum=max(num,maxNum)
    print(maxNum)
    
def isCompleteSquare(num):
    half=num//2
    for i in range(0, half+1):
        for j in range(0, half+1):
            if (i+j)**2==num:
                return True
    return False

if __name__=='__main__':
    find_maxNotcompleteSquare()