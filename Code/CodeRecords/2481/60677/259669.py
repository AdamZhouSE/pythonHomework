times=int(input())
def do():
    line0=input().split()
    line1=input().split()
    line2=input().split()
    line1=set(line1)
    line2=set(line2)
    line1.intersection_update(line2)
    print(line1.__len__())
for i in range(times):
    do()