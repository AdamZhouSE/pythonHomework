nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
print(N)
print(M)
selected_zheng=[]
selected_fu=[]
ls=[]
result=0
while True:
    try:
        s = input()
        ls.append(s.split(" "))
    except EOFError:
        break
for i in range(len(ls)):
    ls[i][0]=int(ls[i][0])
    ls[i][1]=int(ls[i][1])
for i in range(len(ls)):
    if not selected_zheng.__contains__(ls[i][0]) and not selected_fu.__contains__(ls[i][1]):
        selected_zheng.append(ls[i][0])
        selected_fu.append(ls[i][1])
        result=result+1
print(result)

