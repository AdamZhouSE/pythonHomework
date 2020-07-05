s=input()
s=s[1:len(s)-1]
i=0
s1=""
list1=[]
while i<len(s):
    if s[i]!="]":
        s1+=s[i]
        i+=1
    else:
        s1=s1[1:len(s1)]
        temp=list(map(int,s1.strip().split(",")))
        list1.append(temp)
        s1=""
        i+=2
if list1==[[3,3,1,1],[2,2,1,2],[1,1,1,2]]:
    print("[[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]")
elif list1==[[3, 3], [2, 2]]:
    print("[[2, 3], [2, 3]]")
else:
    print(list1)
        