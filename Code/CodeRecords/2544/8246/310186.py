class Point: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

def onSegment(p, q, r): 
	if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
		(q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
		return True
	return False

def orientation(p, q, r): 
	
	val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
	if (val > 0): 
		
		return 1
	elif (val < 0): 
		
		return 2
	else: 
		
		# Colinear orientation 
		return 0

# The main function that returns true if 
# the line segment 'p1q1' and 'p2q2' intersect. 
def doIntersect(p1,q1,p2,q2): 
	
	# Find the 4 orientations required for 
	# the general and special cases 
	o1 = orientation(p1, q1, p2) 
	o2 = orientation(p1, q1, q2) 
	o3 = orientation(p2, q2, p1) 
	o4 = orientation(p2, q2, q1) 

	# General case 
	if ((o1 != o2) and (o3 != o4)): 
		return True

	# Special Cases 

	# p1 , q1 and p2 are colinear and p2 lies on segment p1q1 
	if ((o1 == 0) and onSegment(p1, p2, q1)): 
		return True

	# p1 , q1 and q2 are colinear and q2 lies on segment p1q1 
	if ((o2 == 0) and onSegment(p1, q2, q1)): 
		return True

	# p2 , q2 and p1 are colinear and p1 lies on segment p2q2 
	if ((o3 == 0) and onSegment(p2, p1, q2)): 
		return True

	# p2 , q2 and q1 are colinear and q1 lies on segment p2q2 
	if ((o4 == 0) and onSegment(p2, q1, q2)): 
		return True

	# If none of the cases 
	return False

def solve():
    num = int(input())

    for _ in range(num):
        x1, y1, x2, y2 = [int(i) for i in input().split(' ')]
        x3, y3, x4, y4 = [int(i) for i in input().split(' ')]
        res = doIntersect(
            Point(x1,y1),
            Point(x2,y2),
            Point(x3,y3),
            Point(x4,y4)
        )
        if(res):
            print(1)
        else:
            print(0)

solve()