import sys

n=int(sys.stdin.readline())
for i in range(0,n):
    num=int(sys.stdin.readline())
    people=[]
    current=0
    for j in range(1,num+1):
        people.append(j)
    for j in range(0,num-1):
        now=people[current]
        del people[(current+1)%len(people)]
        index=people.index(now)
        current=(index+1)%len(people)
    for item in people:
        print(item)