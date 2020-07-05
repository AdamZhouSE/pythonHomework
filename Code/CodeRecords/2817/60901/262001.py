def question30():
    num = int(input())
    l = list(map(int, input().split()))
    for i in range(num):
        if l[l[l[i] - 1] - 1] - 1 == i:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    print(question30())