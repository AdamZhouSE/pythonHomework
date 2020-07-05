rec1=list(map(int,input().split(',')))
rec2=list(map(int,input().split(',')))
if max(rec1[0],rec2[0])<min(rec1[2],rec2[2]) and max(rec1[1],rec2[1])<min(rec1[3],rec2[3]):
    print(True)
else:
    print(False)