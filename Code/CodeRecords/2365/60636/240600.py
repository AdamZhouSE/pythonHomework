import itertools

def permutation(li):
    return list(itertools.permutations(li))
number=int(input())
lists=[]
for i in range(number):
    source=[]
    num=int(input())
    lis=input().split(" ")
    for i in range(num):
        source.append(int(lis[i]))
    lists.append(source)
for i in range(len(lists)):
    possiable=[]
    a=permutation(lists[i])
    for i in range(len(a)):
        answer=""
        for x in a[i]:
            answer=answer+str(x)
        possiable.append(answer)
    print(max(possiable))
        
        