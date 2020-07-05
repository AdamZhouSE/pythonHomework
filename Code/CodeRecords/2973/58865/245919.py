s=input()#密文
n=int(input())#密码个数
password=[]#密码列表
for i in range(n):
    password.append(input())

#全排列算法
def all_permutation_arr(stra):
    lsta=list(stra)
    arr=[]
    #从第i个开始，分别与i+1,i+2...交换产生新的排列
    for i in range(len(stra)):
        lsta_copy=lsta
        swap_arr=[]
        for j in range(i,len(stra)):
            lsta_copy[i],lsta_copy[j]=lsta_copy[j],lsta_copy[i]
            s=''
            for k in lsta_copy:
                s+=k
            swap_arr.append(s)
        for q in swap_arr:
            arr.append(q)
    return arr

count=0
for i in password:
    for j in all_permutation_arr(i):
        if j in s:
            count+=1
print(count)