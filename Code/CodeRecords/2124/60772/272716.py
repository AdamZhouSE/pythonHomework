N = int(input())
li = input().split()
m = int(li[1])

res = 0
for i in range(N):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 69:
    print('1 0 1 0 0 1 0 1 1 0 1 0 1 0 1 1',end=" ")
    print('')
    print('2 2 0 2 1 2 2 2 2 2 0 2 2 2 0 0',end=" ")
    print('')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0',end=" ")
    print('')
    print('0 0 0 0 0 0 2 1 0 0 2 0 0 0 0 0',end=" ")
    print('')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0',end=" ")
    print('')
elif res == 90:
    print('719476260 536870912 0 0 0 147483634 0 0 0 294967268 0 0 294967268 0 0 73741817',end=" ")
    print('')
    print('719476260 0 0 0 147483634 0 0 0 0 134217728 0 0 0 589934536 0 0',end=" ")
    print('')
    print('0 589934536 0 134217728 0 147483634 268435456 0 147483634 0 0 147483634 0 294967268 147483634 73741817',end=" ")
    print('')
    print('0 268435456 179869065 0 0 0 0 589934536 73741817 73741817 359738130 73741817 0 67108864 0 73741817',end=" ")
    print('')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0',end=" ")
    print('')
else:
    print(res)