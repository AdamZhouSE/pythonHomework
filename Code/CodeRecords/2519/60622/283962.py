s=input()
list_in=list(map(int,s[1:len(s)-1].split(',')))
list_in.sort()
n=len(list_in)
ans=[]
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for q in range(j+1,n):
            if list_in[i]+list_in[j]>list_in[q] and list_in[i]+list_in[q]>list_in[j] and list_in[j]+list_in[q]>list_in[i]:
                ans.append(list_in[i]+list_in[j]+list_in[q])
                break
ans.sort()
if len(ans)!=0:
    print(ans[-1])
else:
    print(0)