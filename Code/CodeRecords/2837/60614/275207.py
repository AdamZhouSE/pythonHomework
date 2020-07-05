init=[int(x) for x in input().split()]
length=init[0]
minimum=init[1]
maximum=init[2]
miniSum=pow(2,minimum)-1+length-minimum
maxiSum=pow(2,maximum)-1+pow(2,maximum-1)*(length-maximum)
print(str(miniSum)+" "+str(maxiSum))