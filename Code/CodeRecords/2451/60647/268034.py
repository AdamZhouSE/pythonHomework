list=input().split(",")
n=int(input())
a=0
for i in range(len(list)):
    if n==int(list[i]):
        print(i)
        a=1
        break
if a==0:
    for i in range(len(list)-1):
        if n>int(list[i])and n<int(list[i+1]):
            print(i+1)
    if n>int(list[len(list)-1]):
        print(len(list))
    if n<int(list[0]):
        print(0)