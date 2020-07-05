string=input()
string=string[1:len(string)-1]
s=[]
s=string.split(",")
for i in range(len(s)):
    if s[i]!='null':
        s[i]=int(s[i])
n=[]
n.append(1)#该数组用于储存第i层及之前的满二叉树的结点数

p=1
while n[len(n)-1]<len(s):
    p=p*2
    this=n[len(n)-1]+p
    n.append(this)
#print(n)
if string.__contains__("null"):
    index=s.index('null')
else:
    index=len(s)
#print("index",index)
for i in range(1,len(n)):
    #print(n[i])
    if index>n[i-1] and index<=n[i]:
        if not(string.__contains__("null")) and index<n[i]:
            i=i-1  #非满的完全二叉树
        #print("yes",n[i])
        break
print(i+1)





