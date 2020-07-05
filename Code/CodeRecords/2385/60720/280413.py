size=int(input())
def sum(num):
    if num==1:
        return 2
    if num==2:
        return 3
    return sum(num-1)+sum(num-2)
for k in range(size):
    num=int(input())
    print(sum(num))
