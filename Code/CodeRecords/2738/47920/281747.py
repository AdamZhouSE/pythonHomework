li_inp = []
while True:
    try:
        inp = input()
        if(inp !="]" and inp !="["):
            li_inp.append((eval(inp)))
    except:
        break

for i in range(len(li_inp)-1):
    li_inp[i] = li_inp[-1]
#print(li_inp)
if(len(li_inp) == 0):
    print("0")
else:
    print(6)