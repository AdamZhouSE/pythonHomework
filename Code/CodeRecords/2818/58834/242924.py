a=input()
b=input()
a_list=a.split()
b_list=b.split()
n=int(a_list[0])
x=int(a_list[1])
for number in range(0,n):
    for d in range(number+1,n):
        if int(b_list[number]) > int(b_list[d]):
            i = b_list[number]
            b_list[number] = b_list[d]
            b_list[d] = i
    else:
        continue
min_time=0
if x > n:
    for q in range(0,n):
        min_time+=int(b_list[q])*x
        x=x-1
else:
    d=0
    while x>1:
        min_time+=int(b_list[d])*x
        d+=1
        x=x-1
    for w in range(x,n):
       min_time+=int(b_list[w])
print(min_time)
