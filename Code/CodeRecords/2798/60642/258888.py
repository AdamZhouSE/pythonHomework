input()
a = input().split()
list = []
for i in range(len(a)):
    list.append(int(a[i]))
listsum = sum(list)/3
middlesum = 0
flexible = 0
thrid = 0
for i in range(len(list)):
    middlesum = middlesum+list[i]
    if( middlesum==listsum ):
        if(i<len(list)-2 and list[i+1]==0 and i!=0):
            print(i)
            flexible+=1
        else:
            middlesum=0
            thrid = thrid+1
if(thrid==3):
    print(flexible+1)
else:
    print(0)