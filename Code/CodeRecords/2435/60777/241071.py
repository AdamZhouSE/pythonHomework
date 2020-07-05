temp=input().split()
n=int(temp[0])
m=int(temp[1])
word=[]

for i in range(n):
    word.append(input())

def enquiry():
    for i in range(m):
        temp=input().split()
        start=int(temp[0])-1
        end=int(temp[1])-1
        print(findLast(start,end))
        
def findLast(x,y):
    last=word[x]
    for i in range(y-x):
        last=compare(last,word[x+1+i])
    return last    
    
def compare(x,y):
    w1=x.lower()
    w2=y.lower()
    time=min(len(w1),len(w2))
    for i in range(time):
        if(w1[i]<w2[i]):
            return y
        elif(w1[i]>w2[i]):
            return x
    return x

enquiry()