num=int(input())
for i in range(num):
    target=int(input())
    if target**0.5%1==0:
        print(1)
    else:
        print(0)