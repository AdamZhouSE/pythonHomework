def swap(string,a):
    char1=string[a]
    char2=string[a+1]
    out=""
    out=string[0:a]+char2+char1+string[a+2:]
    return out
l=int(input())
string=input()
visited=[]
num=[]
ji=0
for i in string:
    if i not in visited:
        visited.append(i)
        num.append(string.count(i))
for i in num:
    if i%2!=0:
        ji+=1

if(l%2==0 and ji!=0):
    print("Impossible")
elif(l%2!=0 and ji>1):
    print("Impossible")
else:
    count=0
    index=l-1
    for i in range(0,int(l/2)):
        char=string[i]
        for j in range(index,int(l/2)-1,-1):
            if string[j]==char:
                for k in range(j,index):
                    string=swap(string,k)
                    count+=1
                break
        index-=1
    print(count)