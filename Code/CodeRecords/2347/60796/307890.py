nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
selected_zheng=[]
selected_fu=[]
ls=[]
zheng_can_fu=[]
while True:
    try:
        s = input()
        ls.append(s.split(" "))
    except EOFError:
        break
i=0
while i<len(ls):
    ls[i][0]=int(ls[i][0])
    ls[i][1]=int(ls[i][1])
    if ls[i][0]>M or ls[i][1]<M+1:
        del ls[i]
        i=i-1
    i=i+1
for i in range(M):
    this=[]
    for j in range(len(ls)):
        if ls[j][0]==i+1:
            this.append(ls[j][1])
    zheng_can_fu.append(this)
for i in range(M):
    this_zheng=i+1
    if len(zheng_can_fu[i])>0:
        can=False
        this_can=[]
        for j in range(len(zheng_can_fu[i])):
            this_fu=zheng_can_fu[i][j]
            if not selected_fu.__contains__(this_fu):
                this_can.append(this_fu)
                can=True
        if can:
            have=False
            for j in range(len(this_can)):
                exits=False
                for k in range(len(zheng_can_fu)):
                    if k!=i and zheng_can_fu[k].__contains__(this_can[j]):
                        exits=True
                        break
                if not exits:
                    selected_fu.append(this_can[j])
                    selected_zheng.append(this_zheng)
                    have=True
                    break
            if not have:
                selected_zheng.append(this_zheng)
                selected_fu.append(this_can[0])
        if not can:
            for j in range(len(zheng_can_fu[i])):
                this_fu = zheng_can_fu[i][j]
                ind=selected_fu.index(this_fu)
                this_fu_zheng=selected_zheng[ind]
                for k in range(len(zheng_can_fu[this_fu_zheng-1])):
                    another_fu=zheng_can_fu[this_fu_zheng-1][k]
                    if not selected_fu.__contains__(another_fu):
                        selected_fu[ind]=another_fu
                        selected_fu.append(this_fu)
                        selected_zheng.append(this_zheng)
                        break
                if selected_zheng.__contains__(this_zheng):
                    break
    
print(len(selected_fu))


