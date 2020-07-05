def question26():
    num = int(input())
    length = list(map(int,input().split()))
    length.sort()
    sum1 = sum(length[0:num//2])
    sum2 = sum(length[num//2:])
    return pow(sum1,2)+pow(sum2,2)

if __name__ == '__main__':
    print(question26())