cnt=int(input())
list1 = list(map(int, input().split(' ')))
dict1={}
dict1[1]=0
dict1[0]=0
for i in list1:
    if i %2 ==0 :
        dict1[0]=dict1.get(0,0)+1
    else:
        dict1[1]=dict1.get(1,0)+1
print(min(dict1[1] , dict1[0]))