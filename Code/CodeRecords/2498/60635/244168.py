src = input()
array = [int(x) for x in src[1:len(src)-1].split(',')]
odds=[x for x in array if x%2==1]
evens=[x for x in array if x%2==0]
for i in range(len(odds)):
    array[2*i]=evens[i]
    array[2*i+1]=odds[i]
print(array)