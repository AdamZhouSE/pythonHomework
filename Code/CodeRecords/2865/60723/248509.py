number=int(input())
large=int(input())
list=[]
for i in range(number):
    list.append(int(input()))
list.sort(reverse=True)
count=0
while large>0:
    large=large-list[count]
    count=count+1
print(count)