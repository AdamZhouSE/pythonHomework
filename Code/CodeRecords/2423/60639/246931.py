def solution():
    inp1=input().split(' ')
    arr1=input().split(' ')
    arr2=input().split(' ')
    num2=int(inp1[1])
    count=0
    for i in range(num2):
        if arr2[i] in arr1:
            count+=1
    if count==num2:
        print('Yes')
    else:
        print('No')
def main():
    T=int(input())
    for i in range(T):
        solution()

main()

