start=input()
s=start[1:len(start)-1]
list=s.split(',')

num=len(list)
max=0
for i in range(num):
    #print(int(start[2*i+1]))
    #print(start[2*i+1])
    item=int(list[i])
    #print(item)
    list[i]=item
for i in range(num-1):
    for j in range(num-1):
        if list[j]>list[j+1]:
            t=list[j+1]
            list[j+1]=list[j]
            list[j]=t
if num<2: print(0)
else:
    for k in range(num-1):
        n=list[k+1]-list[k]
        if n>max:
            max=n
    print(max)