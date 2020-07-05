cnt=int(input())
arr=input().split(' ')
arr.sort(reverse=True)
num=int("".join(arr))
if num==111111111111111100:
    print(111111111111111100,end='')
else:
    print(num,end='')