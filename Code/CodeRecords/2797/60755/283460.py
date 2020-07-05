num = input()
all = input().split(" ")
for i in range(len(all)):
    all[i] = int(all[i])
if len(all)==1 and all[0]==0 :
    print("UP")
elif len(all)==1 and all[0] == 15:
    print("DOWN")
elif len(all)<=1:
    print(-1)
elif all[-1] == 15:
    print("DOWN")
elif all[-1] == 0 and all[-1]-all[-2]<0:
    print("UP")
elif all[-1]-all[-2]<0:
    print("DOWN")
elif all[-1]-all[-2]>0:
    print("UP")