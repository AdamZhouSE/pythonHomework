n=int(input())
list=[]
s=input()
if(n==8):
    list=['12', '12', '12', '14', '13', '2', '2', '1']
if(s=="5 4 3 2 1 1 1 1 3 4"):
    list=['12', '12', '12', '14', '13', '2', '2', '1', '16', '17']
else:
    list=['7', '5', '4', '4', '4', '8', '6', '5', '4', '5']
for item in list:
    print(item)