a=input()
list=a.split(' ')
b=int(list[0])
c=int(list[1])
d=-1

hash = []
income = []

for i in range(b):
    hash.append(-1)

for i in range(c):
    e = input()
    if(hash[int(e)%b]==-1):
        hash[int(e) % b]=int(e)
    else :
        d=i+1
        break

print(d)