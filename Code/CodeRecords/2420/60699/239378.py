cnt=int(input())
def func(e):
    while e > 0:
        if e % 10 == 0:
            return False
        e//=10
    return True
for i in range(1,cnt//2+1):
    if func(i) and func(cnt-i):
        list1=[]
        list1.append(i)
        list1.append(cnt-i)
        print(list1)
        break