import collections
string=input()
count=collections.Counter(string)
out=[0]*10
out[0]=count["z"]
out[2]=count["w"]
out[4]=count["u"]
out[6]=count["x"]
out[8]=count["g"]
out[3]=count["h"]-out[8]
out[5]=count["f"]-out[4]
out[7]=count["s"]-out[6]
out[9] = count["i"] - out[5] - out[6] - out[8]
out[1] = count["n"] - out[7] - 2 * out[9]
for i in range(0,10):
    if out[i]!=0:
        for j in range(0,out[i]):
            print(i,end="")
print()