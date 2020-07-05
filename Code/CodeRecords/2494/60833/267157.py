list1=list(str(input())[1:-1].split(","))
list1 = list(map(int, list1))
s=len(list1)
num=0
for i in range(0,s-1):
    for j in range(i+1,s):
        if (i<j)&(list1[i]>2*list1[j]):
            num=num+1
print(num)