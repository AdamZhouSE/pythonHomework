tomatoSlices = int(input())
cheeseSlices = int(input())

a = (tomatoSlices - 2*cheeseSlices)/2
b = (4*cheeseSlices - tomatoSlices)/2
if a == int(a) and b == int(b) and a >= 0 and b >= 0:print([int(a),int(b)]) 
else:print([])
 