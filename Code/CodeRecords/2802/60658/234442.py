n,m = [int(x) for x in input().split()]
li = list(enumerate([int(x) for x in input().split()],start=1))
while len(li)>1:
    if li[0][1]-m<=0:
        del li[0]
    else:
        li.append(tuple([li[0][0],li[0][1]-m]))
        del li[0]
print(li[0][0])
        

