def portion(index,start):
    for i in range(index, len(start) - 1):
        re = []
        str1 = start[0:i - 1]
        str2 = start[i:]
        str1.sort()
        str2.sort()
        for j in range(0, len(str1)):
            re.append(str1[j])
        for j in range(0, len(str2)):
            re.append(str2[j])
        if re == arr:
            start = start[i:]
            break
    return start
arr=eval(input())
start=arr
number=1
arr.sort()
if arr==start:
    print(number)
else:
   while True:
      i=2
      a=""
      mark=0
      while i<len(start)-1:
          a=portion(i,start)
          if a==start:
              i=i+1
          else:
              mark=1
              number=number+1
              break
      start=a
      if len(start)==2:
          break
      elif mark==0:
          break
   print(number)