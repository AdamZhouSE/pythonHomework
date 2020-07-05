n=int(input())
this=0
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
book=int(input())
number=list(input().split(" "))
for i in range(book):
    number[i]=int(number[i])
for i in range(book):
    for j in range(n):
        this=this+num[j]
        if number[i]<=this:
            print(j+1)
            break
    this=0