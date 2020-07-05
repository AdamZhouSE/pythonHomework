rows_num=int(input())
s=input()
for i in range(1,rows_num):
    s+=','
    s+=input()
arr=eval(s)
target=int(input())
for i in arr:
    if(i==target):
        print(True)
        break
    elif (i>target):
        print(False)
        break