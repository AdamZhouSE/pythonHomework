def sub(str_,max_,min_):
    list=[]
    for i in range(len(str_)-min_+1):
        for j in range(i+min_,min(i+max_,len(str_))+1 ):
            list.append(str_[i:j])
    return list

def di(str_):
    list=[]
    for i in str_:
        if i not in list:
            list.append(i)
    return len(list)

str_=input()
maxLetters=int(input())
minSize=int(input())
maxSize=int(input())
l=sub(str_,maxSize,minSize)
l_=[]
for i in l:
    if di(i)<=maxLetters:
        l_.append(i)
max=0
for i in l_:
    if l_.count(i)>max:
        max=l_.count(i)
print(max)