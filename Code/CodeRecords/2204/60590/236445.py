def pri(num):
    if num==1:
        return '1'
    else:
        return pri(num-1)+' '+str(num)

t = int(input())
for i in range(t):
    num = int(input())
    print(pri(num)+' ')