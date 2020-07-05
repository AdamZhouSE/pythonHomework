numbers=int(input())
lists=[]
for i in range(numbers):
    l=input()
    lists.append(list(map(int,input().split(" "))))
#list1=[3,5,4]
#list2=[6,4,9,7,8]
def istri(a,b,c:int):
    if a+b>c and a+c>b and b+c>a and abs(a-b)<c and abs(a-c)<b and abs(b-c)<a:
        return True
    else:
        return False

def count_tri(list0:list):
    res=0
    length=len(list0)
    for i in range(length):
        for j in range(i,length):
            if j>i:
                for m in range(j,length):
                    if m>j:
                        if istri(list0[i],list0[j],list0[m]):
                            res=res+1
    return res
for i in lists:
    print(count_tri(i))