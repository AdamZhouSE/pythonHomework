numbers=list(map(int,input()[1:-1].split(",")))
begin=0
end=len(numbers)
while begin<len(numbers) and numbers[begin]==min(numbers[begin:end]):
    begin=begin+1
if begin==end:
    print(0)
else:
    while  end>0 and numbers[end-1]==max(numbers[begin:end]):
        end=end-1
    print(end-begin)