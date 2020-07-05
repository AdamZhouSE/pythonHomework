n=input()
n=n[1:len(n)-1]
list=n.split(',')
li=""
m=0
for i in range(0,len(list)-1):
    for k in range(i+1,len(list)):
      if(int(list[i])>int(list[k])):
          m=list[i]
          list[i]=list[k]
          list[k]=m
for i in range(len(list)):
    li=li+", "+list[i]
print('['+li[2:len(li)]+']')