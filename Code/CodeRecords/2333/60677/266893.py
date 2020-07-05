import math
x=int(input())
y=int(input())
bound=int(input())
answer=[]
for i in range(int(math.log(bound,x)+2)):
    for j in range(int(math.log(bound,y)+2)):
        strong=x**i+y**j
        if strong<=bound:
            answer.append(strong)
answer=list(set(answer))
answer.sort()
print(str(answer))