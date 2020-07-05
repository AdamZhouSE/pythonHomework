n=int(input())-1
num=1
list=input().split(' ')
smith_score=int(list[0])+int(list[1])+int(list[2])+int(list[3])
for i in range(0,n):
    list1=input().split(' ')
    score=int(list1[0])+int(list1[1])+int(list1[2])+int(list1[3])
    if score>smith_score:
        num=num+1
print(num)