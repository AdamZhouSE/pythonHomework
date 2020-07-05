n=int(input())
num_list=list(map(int,input().split()))
output="NO"
for i in range(n):
    if num_list[num_list[num_list[i]-1]-1]==i+1:
        output="YES"
        break
print(output)