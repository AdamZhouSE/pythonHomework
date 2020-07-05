n=int(input())
a=input()
list=a.split()
s=""
list.sort(reverse=True)
for i in range(0,len(list)):
    s=s+list[i]
print(int(s),end='')