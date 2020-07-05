def permutation(s_list, start, last):
    if start >= last:
        if s_list[0]!='0':
            arr.append("".join(s_list))
    else:
        for i in range(start, last):
            s_list[i], s_list[start] = s_list[start], s_list[i]
            permutation(s_list, start + 1, last)
            s_list[i], s_list[start] = s_list[start], s_list[i]

def judge(num):
    temp=0
    while pow(2, temp)<num:
        temp+=1
    if pow(2, temp)==num:return True
    else:return False

n=list(input())
arr=[]
permutation(n,0,len(n))
flag="false"
for i in arr:
    if judge(int(i)):
        flag="true"
print(flag)