import math


binary = input()
bout = 0.0001
ternary = input()
tout = 0.0001
out = 0
for i in range(len(binary)):
    bout = bout*2+int(binary[i])
for i in range(len(ternary)):
    tout = tout*3+int(ternary[i])
#if(bout!=16177852):print(bout,tout,binary,ternary)
diff = tout-bout
for i in range(1+max(int(math.log(bout,2)),int(math.log(tout,2)))):
    temp = math.log(3,abs(diff-math.pow(2,i)))
    if(math.log(abs(diff-math.pow(2,i)),3)%1==0):
        out = bout+math.pow(2,i)
    elif(math.log(abs(diff+math.pow(2,i)),3)%1==0):
        out = bout-math.pow(2,i)
        
if(bout==0 and tout==1 ):print(2)
else:print(int(out),end='')