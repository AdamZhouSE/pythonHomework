def func(A,X):
    low=0
    high=len(A)-1
    while high>low:
        if A[low]+A[high]==X: 
            return "Yes"
        elif A[low]+A[high]>X: 
            low += 1
        else: 
            high -= 1
    return "No"



if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        inp1 = input().split()
        idx = int(inp1[1])
        list1 = input().split(" ")
        for j in range(len(list1)):
            list1[j] = int(list1[j])
        print(func(list1,idx))