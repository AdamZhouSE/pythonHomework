a=input()
b=input()
def find(s:str,lis:list):
    for i in range(len(s)):
        j=i
        while j<len(s):
            lis.append(s[i:j+1])
            j+=1
a1=[]
b1=[]
find(a,a1)
find(b,b1)
count=0
for i in a1:
    count+=b1.count(i)
print(count)