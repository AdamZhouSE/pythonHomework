str = input();
arr = list(str);
if(arr[0] == '-'):
	arr = arr[1:]
	arr.reverse()
	str = "-" + "".join(arr);
else:
	arr.reverse()
	str = "".join(arr);
print(int(str));