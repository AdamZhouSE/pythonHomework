def solve(boy,girl,res):
    if len(boy)==0 or len(girl)==0:
        return res
    if abs(boy[0]-girl[0])<=1:
        return solve(boy[1:],girl[1:],res+1)
    elif boy[0]<girl[0]:
        return solve(boy[1:],girl,res)
    else:
        return solve(boy,girl[1:],res)
   
input()
boy = input().split(" ")
for i in range(len(boy)):
    boy[i] = int(boy[i])
input()
girl = input().split(" ")
for i in range(len(girl)):
    girl[i] = int(girl[i])
boy.sort()
girl.sort()
res = 0

print(solve(boy,girl,res))
    