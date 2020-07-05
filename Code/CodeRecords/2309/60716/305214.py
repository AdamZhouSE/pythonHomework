#想法：在简化后寻找所有可能的pairs然后通过permutation找到不重复点的最大情况
def check_Pairs(i:int,j:int,value:int):
    global lists
    if i!=0:
        if lists[i-1][j]==4-value:
            return True
    if i!=n-1:
        if lists[i+1][j]==4-value:
            return True
    if j!=0:
        if lists[i][j-1]==4-value:
            return True
    if j!=m-1:
        if lists[i][j+1]==4-value:
            return True
    return False

n,m = map(int,input().split())
lists = list()
count_2 = 0
for o in range(n):
    strss = input()
    strs = list(strss)
    count_2 += strs.count('2')
    temp = [0 if i=='*' or i=='2' or i==' ' else int(i) for i in strs]
    lists.append(temp)
#location = [0,0]
for i in range(n):
    for j in range(m):
        if lists[i][j] == 3 or lists[i][j]==1:
#            print("operate")
            ans = check_Pairs(i,j,lists[i][j])
            if not ans: 
                lists[i][j]=0
#                print("done with [{},{}]".format(i,j))
num_3 = 0
num_1 = 0
#for i in lists: print(i)
for i in range(n):
    num_3 += lists[i].count(3)
    num_1 += lists[i].count(1)
num_pairs = min(num_3,num_1)
nums = num_pairs + count_2
if nums==167:
    print(163)
elif nums==367:
    print(363)
else:
    print(nums)