number=int(input())
lists=input().split(" ")
source=[]
for i in lists:
    source.append(i)
times=int(input())
questions=[]
for i in range(times):
    questions.append(input().split(" "))
for a in questions:
    all=[]
    for x in source[int(a[0])-1:int(a[1])]:
        if (not x in all):
            all.append(x)
    print(len(all))