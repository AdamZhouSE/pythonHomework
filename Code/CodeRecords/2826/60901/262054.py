
def question32():
    num = int(input())
    l = sorted(map(int, input().split()))
    coin = 0
    for i in range(num-1):
        while l[i] >= l[i+1]:
            l[i+1] += 1
            coin += 1
    return coin

if __name__ == '__main__':
    print(question32())