#05
ori = input().split(" ")
ori.remove("0")
ori.reverse()
for i in range(0,len(ori)-1):
    print(ori[i],end=" ")
print(ori[len(ori)-1],end="")