token_list=list(input())
judge=0
output="NO"
for element in token_list:
    if element=="(":
        judge+=1
    elif element==")":
        judge-=1
    if judge<0:
        output="NO"
        break
if judge==0:
    output="YES"
print(output,end="")