num=input()
list1=[]
for i in range(num):
    word=input()
    list1.append(word)
for i in range(num):
    list1[i]=sorted(list1[i])
out=1
sorted(list1)
for i in range(1,num):
    if list1[i]!=list1[i-1]:
        out=out+1
print(out)