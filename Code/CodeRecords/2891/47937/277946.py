n=input()
b=input().split(" ")

shuzu=[]
i=0
while i<len(b):
    shuzu.append(int(b[i]))
    i=i+1
  

Max1=max(shuzu)
i=0
money=0
while i<len(shuzu):
    money+=Max1-shuzu[i]
    i=i+1

print(money)