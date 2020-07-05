
def preorder(str,lst):
    lst.remove(str)
    if(str[0]=='*'):
        return
    else:
        print(str[0],end="")
        if str[1]!="*":
            next=[i for i ,x in enumerate(lst) if x.find(str[1])!=-1]
            left=lst[next[0]]
            preorder(left,lst)
        if str[2]!="*":
            next=[i for i ,x in enumerate(lst) if x.find(str[2])!=-1]
            right=lst[next[0]]
            preorder(right,lst)

NUM=int(input())
lst=[input() for i in range(NUM)]
if len(lst)==0:
    print("这是一个空树")
    print("就是一个没用的树")
else:
    preorder(lst[0],lst)
