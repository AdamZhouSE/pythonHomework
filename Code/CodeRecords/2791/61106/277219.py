n=int(input())
stage=input().split()
total=0
result=[]
for i in range(n):
    if stage[i]=='1':
        total += 1
        result.append(stage[i-1])
result=result[1:]+result[:1]
print(total)
print((" ").join(result))