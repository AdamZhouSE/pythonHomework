word=input()
number=0
list1=list(word)
left=0
right=0
for i in range(len(list1)):
    if list1[i]=="A":
        for j in range(i):
            if list1[j]=="Q":
                left=left+1
        for k in range(i,len(list1)):
            if list1[k]=="Q":
                right=right+1
    number=number+left*right
    left=0
    right=0
print(number,end="")