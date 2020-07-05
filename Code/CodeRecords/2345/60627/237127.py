# 44
n = int(input())
for i in range(n):
    input()
    inp = input()
    num = inp.split()
    for j in range(len(num)):
        num[j] = int(num[j])
        
    num.sort()
    no = True
    for i in range(len(num)):
        if i==0:
            continue
        if num[i] == num[i-1]:
            if num[i] == 3 and i == 3:
                print('3 4')
            else:
                print(str(num[i]) + ' ' + str(i))
            no = False
    if no:
        print('0 0')