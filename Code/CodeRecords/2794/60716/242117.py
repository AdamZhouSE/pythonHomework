level = int(input())
str1 = input().split(' ')
bookcount = [int(i) for i in str1]
need = int(input())
str2 = input().split(' ')
number = [int(i) for i in str2]
adders = list()
adders.append(0)
add = 0
answer = list()
for i in bookcount:
    add+=i
    adders.append(add)
for i in number:
    for j in range(len(adders)):
        if i>adders[j] and i<=adders[j+1]:
            answer.append(j+1)
for i in answer:
    print(i)