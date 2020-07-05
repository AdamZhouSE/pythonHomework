num=input()
for i in range(num):
    rawInputs=input().split(' ')
    lenA=rawInputs[0]
    lenB=rawInputs[1]
    ind=rawInputs[2]
    A=input().split(' ')
    B=input().split(' ')
    arr=A+B
    arr.sort()
    print(arr[ind-1])