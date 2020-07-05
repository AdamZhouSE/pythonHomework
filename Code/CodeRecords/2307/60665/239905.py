test_num = int(input());
while test_num>0 :
	length = int(input());
	origin = input();
	list = origin.split(" ");
	mark = [];
	elements = [];
	flag = -1;
	for element in list:
		if element not in elements:
			elements.append(element);
			mark.append(1);
		else:
			index = elements.index(element);
			mark[index] = mark[index] + 1;
			if mark[index]> (length/2):
				flag = elements[index];
	print(flag);