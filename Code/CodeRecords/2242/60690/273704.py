rec1=input().split(",")
rec2=input().split(",")
for i in range(4):
    rec1[i]=int(rec1[i])
    rec2[i]=int(rec2[i])
if rec1[2]<=rec2[0]: print(False)#x2<=x1'
elif rec1[0]>=rec2[2] : print(False)#x2'<=x1
elif rec1[1]>=rec2[3] :print(False)#y1>=y2'
elif rec1[3]<=rec2[1]:print(False)#y1'>=y2
else:print(True)
