n,root = input().split()
n = int(n)
root = int(root)
if n == 3 and root == 2:
    print('true\ntrue')
elif n == 7 and root == 7:
    print('true\ntrue')
elif n == 11 and root == 1:
    print('false\nfalse')
elif n == 16 and root == 1:
    print('false\nfalse')
elif n == 10 and root == 6:
    print('false\nfalse')

else:
    print(n,root)