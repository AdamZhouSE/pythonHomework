points = input().split(",")
s1 = (int(points[2])-int(points[0]))*(int(points[3])-int(points[1]))
s2 = (int(points[6])-int(points[4]))*(int(points[7])-int(points[5]))
l1 = [int(points[0]), int(points[2]), int(points[4]), int(points[6])]
l2 = [int(points[1]), int(points[3]), int(points[5]), int(points[7])]
l1.sort()
l2.sort()
covered = (int(l1[2]) - int(l1[1])) * (int(l2[2])-int(l2[1]))
print(s1+s2-covered)
