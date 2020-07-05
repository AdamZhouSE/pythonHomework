n=eval(input())          //输入N，单词的个数
a=[]                          //列表a用来存单词的
for i in range(n):     //输入N个单词
    s=input()
    a.append(s)           

for i in range(len(a)):  //对每个单词内部排序
    a[i]=sorted(a[i])

ans=1
a=sorted(a)               //对存单词的列表整体排序
for i in range(1,len(a)):       //统计不同的单词
    if a[i]!=a[i-1] :
        ans+=1

print(ans)           