num = int(input())
while num > 0:
    N = int(input())
    str1 = []
    for i in range(1, N+1):
        str1.append('{:b}'.format(i))
    ans = ' '.join(str(i) for i in str1)
    temp = ans.split(' ')
    for i in range(len(temp)):
        print(int(temp[i]), end=' ')
    print()
    num -= 1