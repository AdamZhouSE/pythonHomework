import math

def search(str_a,str_b,start,end):
	if start == end:
		return  start;
	divide = math.ceil( (start+end)/2 );  # 考虑end - start = 1
	if str_a.find(str_b[0:divide]) != -1:
		return search(str_a,str_b,divide,end);
	else:
		return search(str_a,str_b,start,math.floor( (start+end)/2 ));
	
	
limit = input().split(" ");
limti_n = int(limit[0]);
limit_m = int(limit[1]);
str = input();
while(limit_m>0):
	limit_m = limit_m - 1;
	question = input().split(" ");
	str_ab = str[int(question[0])-1:int(question[1])];
	str_cd = str[int(question[2])-1:int(question[3])];
	print(search(str_ab,str_cd,0,len(str_cd)));
