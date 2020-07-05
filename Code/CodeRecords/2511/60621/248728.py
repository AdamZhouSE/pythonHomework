a=input().split()
num=int(a[0])
s=int(a[1])
b=[]
for i in range(num):
    b.append(eval(input()))
for i in range(num):
    head=i
    length=0
    tail=i+length-1
    up=0
    down=0
    while head+length+1<num:
        if up<=s and down<=s and head+length+1<num:
            up+=(b[head+int(length/2)])
            down+=(b[head+length]+b[length+head+1]-b[head+int(length/2)])
        else:
            break
        length += 2
    print(length)
