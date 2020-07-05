row=int(input())
nums=[]

for i in range(row):
    aaa=input()
    l1=aaa.split(",")
    l1= list(map(int, l1))
    for x in l1:
        nums.append(x)

t=int(input())
if t in nums:
    print('True')
else:
    print('False')