chips=input()
chips=list(map(int,chips.split(',')))
dict={}
for i in chips:
    dict[i%2]=dict.get(i%2,0)+1
if(len(dict)==2):
    if dict[0]<dict[1]:
        print(dict[0])
    else:
        print(dict[1])
else:
    print(0)