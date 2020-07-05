lists = list(eval(input()))
H = int(input())
add = 0
for i in lists:
    add+=i
num = add//H if add%H==0 else add//H+1
print(num)