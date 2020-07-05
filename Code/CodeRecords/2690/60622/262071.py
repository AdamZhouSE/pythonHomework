def solve(strings):
    s1=strings.pop()
    s2=strings.pop()
    tem=""
    for i in range(len(s2)):
        if s2[i] in set(s1):
            tem=tem+s2[i]
    return match(tem,s1)

def match(s_long,s_short):
    ans=0
    for i in range(len(s_long)):
        if s_long[i]==s_short[0]:
            if len(s_short)>1:
                ans += match(s_long[i:], s_short[1:])
            else:
                ans+=1
    return ans

num=int(input())
list_ans=[]
for i in range(num):
    num=input().split()
    strings=input().split()
    count=solve(strings)
    list_ans.append(count)
print("\n".join(str(i) for i in list_ans))

# x=[]
# s="sss"
#
# x=len(s)
# print(x)