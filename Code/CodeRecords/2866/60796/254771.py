n=int(input())
l=[]#专门存每一个1右边的0有多少种切割方法
s=input()
s=s.replace(' ','')
s=s.strip('0')#删除首尾的0
for i in range(0,len(s)-1):
    subs=s[i+1:]
    #print(subs)
    if subs[0]=='1':
        continue
    index=subs.index('1')
    l.append(index+1)
    i=i+index+1
re=1
#print(l)
for i in range(len(l)):
    re=re*l[i]
print(re)




