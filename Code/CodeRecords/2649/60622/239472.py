def solve(list):
    string=bin(int(list[0])).replace('0b','')
    left=len(string)-int(list[1])
    right=len(string)-int(list[2])
    if left>right:
        tem=left
        left=right
        right=tem
    string_l=string[:left]
    string_r=string[right+1:]
    string_solve=reverse(string[left:right+1])
    # s=string_l+string_solve+string_r
    # return s
    return string_l+string_solve+string_r
def reverse(string):
    s=""
    for i in range(len(string)):
        if string[i]=="0":
            s=s+"1"
        else:
            s=s+"0"
    return s


num=int(input())
ans_list=[]
for i in range(num):
    l=[]
    l=input().split()
    s=solve(l)
    ans=int("0b"+s,2)
    ans_list.append(ans)
print("\n".join(str(i) for i in ans_list))



