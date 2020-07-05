import math

def bucketSort(targetArr):
	if len(targetArr)<2:
		return 0;
	
	minN = targetArr[0];
	maxN = targetArr[0];
	for element in targetArr:
		if element<minN:
			minN = element;
		if element>maxN:
			maxN = element;
	
	buckets = [];
	for i in range(0,len(targetArr)):
		bucket = [];
		buckets.append(bucket);
		
	for element in targetArr:
		index = math.floor( (element-minN)*(len(targetArr)-1) / (maxN-minN) );
		if len(buckets[index]) == 0:
			buckets[index].append(element);
		elif len(buckets[index]) == 1:
			if element<buckets[index][0]:
				temp = buckets[index][0];
				buckets[index][0] = element;
				buckets[index].append(temp);
			else:
				buckets[index].append(element);
		else:
			if element<buckets[index][0]:
				buckets[index][0] = element;
			if element>buckets[index][1]:
				buckets[index][1] = element;
	
	left = buckets[0][0];
	maxDiff = 0;
	for bucket in buckets:
		if len(bucket) > 0:
			temp = bucket[0] - left;
			if temp > maxDiff:
				maxDiff = temp;
			if len(bucket) > 1:
				left = bucket[1];
			else:
				left = bucket[0];
				
	return maxDiff;

if __name__ == '__main__':
    print(bucketSort(eval(input())));