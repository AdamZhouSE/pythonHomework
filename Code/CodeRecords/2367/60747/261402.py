n=int(input())
str="1"
while True:
    if int(str)%n==0:
        print(len(str))
        break
    str=str+'1'
    if len(str)>=10:
        print(-1)
        break
