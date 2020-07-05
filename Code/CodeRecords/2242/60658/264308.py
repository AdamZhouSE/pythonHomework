li1 = [int(x) for x in input().split(",")]
li2 = [int(x) for x in input().split(",")]
x1,y1 = (li1[0]+li1[2])/2,(li1[1]+li1[3])/2
x2,y2 = (li2[0]+li2[2])/2,(li2[1]+li2[3])/2
k = 0.5*(li1[2]-li1[0]+li2[2]-li2[0])
print(abs(x1-x2)<k and abs(y1-y2)<k)