n=int(input())
s=input()
count=0;
for i in range(n):
    if s[i]=="0":
        count+=1
result="1"
for i in range(count):
    result+="0"
print(result,end="")