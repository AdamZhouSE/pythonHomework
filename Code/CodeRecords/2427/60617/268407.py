def first_redundant():
    T=int(input())
    for i in range(0, T):
        find_Redundant()

def find_Redundant():
    N=int(input())
    arr=list(map(int, input().split(" ")))
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]:
                print(i+1)
                return 
    print(-1)
    
if __name__=='__main__':
    first_redundant()