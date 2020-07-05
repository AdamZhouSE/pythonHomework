def main():
    n=int(input())
    arr1=list(map(int, input().split()))
    arr2=list(map(int, input().split()))
    arr1.sort()
    arr2.sort()
    if arr1==arr2:
        print(1)
    else:
        print(0)

T=int(input())
for i in range(T):
    main()

