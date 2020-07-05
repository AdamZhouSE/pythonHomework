num=int(input())
for i in range(num):
    target=int(input())-1
    if target%2==0:
        print(2**(2**(target//2)))
    else:
        print(2 ** (3 ** (target // 2)))