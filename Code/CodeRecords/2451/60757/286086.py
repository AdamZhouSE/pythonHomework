li=list(eval(input()))
n=int(input())
if(li.count(n)==0):
    li.append(n)
    li=sorted(li)
print(li.index(n))