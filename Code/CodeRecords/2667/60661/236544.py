t=int(input())
for j in range(t):
    il=input()
    i=int(il.split(' ')[0])
    l=int(il.split(' ')[1])
    s=''
    for k in range(l):
       s+='1'
    total=int(s,2)
    print(total-i+1)