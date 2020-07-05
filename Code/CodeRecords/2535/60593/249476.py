import copy
a=eval(input())
ori=a.copy()
a.sort()
st=0
cnt=0
for i in range(len(a)):
    end=i+1
    s_ori=set(ori[st:end])
    s_a=set(a[st:end])
    if(len(s_ori & s_a)==end-st):
        st=i+1
        cnt+=1    
print(cnt)