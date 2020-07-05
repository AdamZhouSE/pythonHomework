input()
list1=list(map(int,input().split(' ')))
res=0
dict={}
for i in list1:
    dict[i]=dict.get(i,0)+1
if 0 not in dict:
    print(-1)
else:
    if 5 not in dict:
        print(0)
    else:
        k=dict[5]//9*9
        str1="5"*k
        if 0 in dict:
            str1=str1+"0"*dict[0]
        print(int(str1))