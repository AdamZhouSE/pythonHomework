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
            print(str(num[i]) + ' ' + str(i+1))
            no = False
    if no:
        print('0 0')