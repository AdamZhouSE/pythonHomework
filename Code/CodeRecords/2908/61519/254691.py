num=int(input())
list1=[]
for i in range(0,num):
    word=input()
    list1.append(word)
for i in range(0,num):
    list1[i]=sotred(list1[i])
sorted(list1)
out=1
for i in range(1,num):
    if list1[i]!=list1[i-1]:
        out=out+1
print(out)