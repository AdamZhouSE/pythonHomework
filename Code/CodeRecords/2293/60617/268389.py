def Kth_least_ele():
    T=int(input())
    for i in range(0, T):
        find_Kth()

def find_Kth():
    n=int(input())
    arr=list(map(int, input().split(" ")))
    K=int(input())
    arr.sort()
    print(arr[K-1])
    
if __name__=='__main__':
    Kth_least_ele()