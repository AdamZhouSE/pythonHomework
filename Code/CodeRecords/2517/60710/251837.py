#元组的和
def fourSumCount(A, B, C, D):
    count = 0
    dic_AB = {}
    for num1 in A:
        for num2 in B:
            if (num1 + num2) in dic_AB:
                dic_AB[num1 + num2] += 1
            else:
                dic_AB[num1 + num2] = 1
    for num3 in C:
        for num4 in D:
            if -(num3 + num4) in dic_AB:
                count += dic_AB[-(num3 + num4)]
    return count
if __name__ == '__main__':
    A=list(map(int,input().split(",")))
    B=list(map(int, input().split(",")))
    C=list(map(int, input().split(",")))
    D=list(map(int, input().split(",")))
    print(fourSumCount(A,B,C,D))