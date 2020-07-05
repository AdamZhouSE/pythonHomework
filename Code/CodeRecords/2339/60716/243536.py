num = int(input())
answer = list()
for i in range(num):
    lens = int(input())
    str = input().split(' ')
    lists = [int(i) for i in str]
    index=0;
    for j in range(len(lists)):
        for k in range(j+1,len(lists)):
            if lists[j]>lists[k]:
                index+=1
    answer.append(index)
for i in answer:
    print(i)