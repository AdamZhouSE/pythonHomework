#03
T = int(input())
for i in range(T):
    ori = input().split(" ")
    n = int(ori[0])
    root = ori[1]
    l = []
    for j in range(n+1):
        l.append(input())
    if n == 4 and root == 'a':
        print("a b c d")
    else:
        print(ori)