n=input()
digit=str(n)
weishu=len(digit)
num=[0]*weishu
for i in range(weishu):
    num[i]=int(digit[i])
m=max(num)
print(m)
output=""
for i in range(m-1):
    element=""
    for j in range(weishu):
        if num[j]>=1:
            element+="1"
            num[j]-=1
        else:
            if element!="":
                element+="0"
    output+=element+" "
final=""
for j in range(weishu):
       if num[j]>=1:
           final+="1"
           num[j]-=1
       else:
           if final!="":
               final+="0"
output+=final
print(output)
    