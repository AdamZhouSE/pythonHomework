str = input();
length = len(str);
mark = [];
for i in range(0,length):
	temp = -1;
	for num in range(0,length):
		if num not in mark:
			if temp == -1:
				temp = num;
			elif str[num]<str[temp]:
				temp = num;
			elif str[num]==str[temp]:
				num_next = num+1;
				temp_next = temp+1;
				while num_next<length and temp_next<length:
					if str[num_next]<str[temp_next]:
						temp = num;
						break;
					elif str[num_next]>str[temp_next]:
						break;
					num_next = num_next+1;
					temp_next = temp_next+1;
				if num_next == length:
					temp = num;
	mark.append(temp);
	print(temp+1,end="");
	if i!=length-1:
		print(" ",end="");
	else:
		print();
