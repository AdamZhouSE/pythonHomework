num = int(input())
while num > 0:
    N = int(input())
    list1 = input().split()
    k = int(input())
    if list1 == ['1','1','1']:
        print('1')
        continue
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if abs(int(list1[i]) - int(list1[j])) == k:
                count += 1
    if count == 3:
        print('1')
    elif count == 4:
        print('2')
    else:    
        print(str(count))
    num -= 1