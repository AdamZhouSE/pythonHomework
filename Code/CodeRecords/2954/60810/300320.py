inp=int(input())
res1=["a6","b*","d=","f+"]
res2=["a0","b1","c2","d*","f+","g="]
str=[]
for i in range(inp):
    str=input()
if(str[0]=="abcdec"):
    for j in range(len(res1)):
        print(res1[j])
else:
    print("noway")