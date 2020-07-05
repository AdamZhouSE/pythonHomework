num=int(input())
for i in range(num):
    rawInputs=input().split(' ')
    lenA=int(rawInputs[0])
    lenB=int(rawInputs[1])
    ind=int(rawInputs[2])
    A=[]
    B=[]
    rawA=input().split(' ')
    rawB=input().split(' ')
    for i in range(lenA):
        A.append(int(rawA[i]))
    for j in range(lenB):
        B.append(int(rawB[j]))
    arr=A+B
    arr.sort()
    print(arr[ind-1])