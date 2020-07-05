global sum
sum=0

def AllCombine(init,before,str):
    if len(str)==1:
        judge=before+str
        if judge in init:
            global sum
            sum=sum+1
    i=0
    while i<len(str):
        if str[i] in str[0:i]:
            i=i+1
            continue
        AllCombine(init,before+str[i],str[0:i]+str[i+1:])
        i=i+1

s=input()
n=int(input())
i=0
while i<n:
    psw=input()
    AllCombine(s,"",psw)
    i=i+1
print(sum)