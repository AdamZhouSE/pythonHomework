def rearrange(tarList):
	front = 0;
	behind = len(tarList) - 1;
	index = 0;
	while index<=behind:
		if index == (behind + 1):
			break;
		if tarList[index] == 0:
			if index != front:
				tarList[index] = tarList[front];
				tarList[front] = 0;
			front = front + 1;
		elif tarList[index] == 2:
			if index == behind:
				break;
			tarList[index] = tarList[behind];
			tarList[behind] = 2;
			behind = behind - 1;
			index = index - 1;
		index = index + 1;
		
if __name__ == '__main__':
    balls = eval(input());
    rearrange(balls);
    print(balls)