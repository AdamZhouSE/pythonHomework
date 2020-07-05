days = int(input())
temp = list(input().split(" "))
lists=[]
source = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in temp:
    lists.append(int(i))

x=0
a=True
while x<len(source) and a:
    if len(lists)==1 and lists[0]==15:
        print("DOWN")
        break
    if len(lists)==1 and lists[0]==0:
        print("UP")
        break
    if len(lists)==1 or len(lists)==0:
        print(-1)
        break
    if lists[0]==source[x]:
        i=0
        while i<len(lists) and x<len(source) and lists[i]==source[x]:
            i=i+1
            x=x+1
            if i==len(lists)-1:
                if source[x+1]-source[x]==1:
                    print("UP")
                    a=False
                else:
                    print("DOWN")
                    a=False
    x=x+1
