str=list(input().split("+"))
for i in range(0,len(str)):
    for j in range(0,len(str)-i-1):
        if int(str[j])>int(str[j+1]):
            str[j],str[j+1]=str[j+1],str[j]
answer=""
for k in range(0,len(str)-1):
    answer=answer+str[k]+"+"
answer=answer+str[-1]
print(answer)